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


# f = open('materials.json', 'w')

materials = {}
textures = {}
headers = { 'User-Agent' : 'Mozilla/5.0' }

blockinfojsonurl = 'http://minecraft-ids.grahamedgecombe.com/items.json'
imageszipurl = 'http://minecraft-ids.grahamedgecombe.com/items.zip'

jsonreq = urllib2.Request(blockinfojsonurl, None, headers)
blockinfojson = urllib2.urlopen(jsonreq).read()

imagezipreq = urllib2.Request(imageszipurl, None, headers)
imagezip = urllib2.urlopen(imagezipreq).read()

z = zipfile.ZipFile(StringIO.StringIO(imagezip))

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

                avgcolor = map(lambda y: sum(y) / float(len(y))/255, zip(*newcolors))
            print avgcolor


# objects = json.loads(blockinfojson)

# for mat in matstatics:
#   if matstatics[mat]["textures"]:
#       for texname in matstatics[mat]["textures"]:
#           matpath = "./blocks/" + texname + ".png"
#           if os.path.exists(matpath) and texname not in textures:
#               with open(matpath, "rb") as image_file:
#                   textures[texname] = base64.b64encode(image_file.read())

# for aobject in objects:
#   material = Material(blockid=(aobject['type'], aobject['meta']),name=aobject['name'], blandname=aobject['name'])
#   materials.update({tofind:material.getDict()})


# materials.update( material.addRest(materials) )

# print "length of materials found on site: " + str(len(materials))

# matsandtex = {"materials":materials,"textures":textures}