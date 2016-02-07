#!/usr/bin/python -B

import urllib2
import re
from PIL import Image
import StringIO
import ast
import json
from staticvalues import *
from material import Material
import os.path
import base64
import zipfile
import os

headers = { 'User-Agent' : 'Mozilla/5.0' }
imageszipurl = 'http://minecraft-ids.grahamedgecombe.com/items.zip'
blockinfojsonurl = 'http://minecraft-ids.grahamedgecombe.com/items.json'
imagezipreq = urllib2.Request(imageszipurl, None, headers)
imagezipfinal = urllib2.urlopen(imagezipreq)
etag = imagezipfinal.info()['ETag']
f = open('materials.json', 'w')

fkey = open('./cache/key', 'r')
fcontent = fkey.read()
etag = etag.translate(None,'\"')



if fcontent != etag or not os.path.isfile('./cache/items.json') or not os.path.isfile('./cache/items.zip'):
    fjson = open('./cache/items.json', 'w')
    fzip = open('./cache/items.zip', 'w')
    jsonreq = urllib2.Request(blockinfojsonurl, None, headers)
    blockinfojson = urllib2.urlopen(jsonreq)

    keycontent = fkey.read()
    fjson.write(blockinfojson.read())
    fzip.write(imagezipfinal.read())
    fzip.close()
    fjson.close()

    fkey = open('./cache/key', 'w')
    fkey.write(etag)
    fkey.close()




materials = {}
textures = {}

fzip = open('./cache/items.zip', 'r')
fjson = open('./cache/items.json', 'r')

itemimagecontents = fzip.read()
itemcontents = fjson.read()

z = zipfile.ZipFile(StringIO.StringIO(itemimagecontents))

avgcolors = []

with z as archive:
    for entry in archive.infolist():
        with archive.open(entry) as afile:
            
            img = Image.open(StringIO.StringIO(afile.read()))
            newcolors = []
            img = img.convert('RGBA')
            allcolors = img.getcolors()
            if allcolors:
                for color in allcolors:
                    for x in xrange(1,color[0]):

                        newcolors.append((color[1][0], color[1][1], color[1][2]))

                avgcolors.append(map(lambda y: sum(y) / float(len(y))/255, zip(*newcolors)))

objects = json.loads(itemcontents)
'name'
for mat in matstatics:
    if matstatics[mat]["textures"]:
        for texname in matstatics[mat]["textures"]:
            matpath = "./blocks/" + texname + ".png"
            if os.path.exists(matpath) and texname not in textures:
                with open(matpath, "rb") as image_file:
                    textures[texname] = base64.b64encode(image_file.read())


for aobject in objects:
    tofind = (aobject['type'], aobject['meta'])
    material = Material(blockid=(aobject['type'], aobject['meta']),name=aobject['name'].encode('ascii','ignore'), blandname=aobject['name'].encode('ascii','ignore'))
    materials.update({tofind:material.getDict()})

# print materials

materials.update( material.addRest(materials) )

print "length of materials found on site: " + str(len(materials))

matsandtex = {"materials":materials,"textures":textures}

f.write(repr(matsandtex))