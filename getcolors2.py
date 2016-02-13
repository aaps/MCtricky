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
f = open('materials.someformat', 'w')

fkey = open('./cache/key', 'r')
fcontent = fkey.read()
etag = etag.translate(None,'\"')



if fcontent != etag or not os.path.isfile('./cache/items.json') or not os.path.isfile('./cache/items.zip'):
    print 'Downloading new values/files since the cache key is changed !!'
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
else:
    print 'Not downloading new values since cache is the same !'




materials = {}
textures = {}

fzip = open('./cache/items.zip', 'r')
fjson = open('./cache/items.json', 'r')

itemimagecontents = fzip.read()
itemcontents = fjson.read()

z = zipfile.ZipFile(StringIO.StringIO(itemimagecontents))

avgcolors = {}

with z as archive:
    for entry in archive.infolist():
        
        idmeta =  tuple(map(int,entry.filename[:-4].split('-')))
        with archive.open(entry) as afile:
            filedata = afile.read()
            img = Image.open(StringIO.StringIO(filedata))

            newcolors = []
            img = img.convert('RGBA')
            allcolors = img.getcolors(1024*2)
            
            if allcolors and len(allcolors) > 1:
                for color in allcolors:
                    if color[1][3] > 0:
                        for x in xrange(1,color[0]):
                            newcolors.append((color[1][0], color[1][1], color[1][2], color[1][3]))

                avgcolor = tuple(map(lambda y: round(sum(y) / float(len(y))/255, 3), zip(*newcolors)))

                avgcolors.update({idmeta:avgcolor})
            else:

                avgcolors.update({idmeta:(0,0,0,1)})




objects = json.loads(itemcontents)
for mat in matstatics:
    if matstatics[mat]["textures"]:
        for texname in matstatics[mat]["textures"]:
            matpath = "./blocks/" + texname + ".png"
            if os.path.exists(matpath) and texname not in textures:
                with open(matpath, "rb") as image_file:
                    textures[texname] = base64.b64encode(image_file.read())


for aobject in objects:
    tofind = (aobject['type'],aobject['meta'])
    if tofind in avgcolors:
        material = Material(color=avgcolors[tofind][0:3],alpha=avgcolors[tofind][3],blockid=(aobject['type'], aobject['meta']),name=aobject['name'].encode('ascii','ignore'), blandname=aobject['name'].encode('ascii','ignore'))
    else:
        print str(tofind) + ' not in there !'
        material = Material(blockid=(aobject['type'], aobject['meta']),name=aobject['name'].encode('ascii','ignore'), blandname=aobject['name'].encode('ascii','ignore'))

    materials.update({tofind:material.getDict()})

materials.update( material.addRest(materials) )

print "length of materials found on site: " + str(len(materials))

matsandtex = {"materials":materials,"textures":textures}

toformat = repr(matsandtex).replace("}", "}\n")



f.write(toformat)