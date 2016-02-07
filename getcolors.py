# #!/usr/bin/python -B

#use getcolors2.py !

# import urllib2
# from bs4 import BeautifulSoup
# import re
# from PIL import Image
# import StringIO
# import ast
# import json
# from staticvalues import *
# from material import Material
# import os.path
# import base64



# f = open('materials.json', 'w')

# materials = {}
# textures = {}
# baseurl = 'http://minecraft-ids.grahamedgecombe.com/'
# cssurl = baseurl + 'stylesheets/bundles/all/1440429950.css'
# imageurl = baseurl + 'images/sprites/items-21.png'

# headers = { 'User-Agent' : 'Mozilla/5.0' }
# htmlreq = urllib2.Request(baseurl, None, headers)
# html = urllib2.urlopen(htmlreq).read()
# cssreq = urllib2.Request(cssurl, None, headers)
# css = urllib2.urlopen(cssreq).read()
# imagereq = urllib2.Request(imageurl, None, headers)
# image = urllib2.urlopen(imagereq).read()

# buff = StringIO.StringIO(image)

# print 'html length: ' + str(len(html))

# im = Image.open(buff)

# print im.size, im.mode

# soup = BeautifulSoup(html, "lxml")
# counter = 0

# for mat in matstatics:
# 	if matstatics[mat]["textures"]:
# 		for texname in matstatics[mat]["textures"]:
# 			matpath = "./blocks/" + texname + ".png"
# 			if os.path.exists(matpath) and texname not in textures:
# 				with open(matpath, "rb") as image_file:
# 					textures[texname] = base64.b64encode(image_file.read())

# for arow in soup.find_all("tr", class_="row"):
	
# 	tofind = arow.div["class"]
# 	name = arow.find_all("span", class_="name")[0].getText().encode('ascii','ignore')
# 	match = re.search(r"[^a-zA-Z](" + tofind[1] +  ")[^a-zA-Z]", css)
# 	num = match.start(1)
	
# 	if len( css[num:num+110].split(" ")[2][1:-2]) > 1:
# 		dimtoget = ast.literal_eval(css[num:num+110].split(" ")[2][1:-2])
# 		cromdim = (0,dimtoget,32,dimtoget+32)
# 		allcolors = im.crop(cromdim).getcolors()
# 		tofind = arow.find_all("td", class_="id")[0].getText()


# 		if ":" in tofind:
# 			tofind = tofind.split(":")
# 			tofind = int(tofind[0]),int(tofind[1])
# 		else:
# 			tofind = int(tofind), 0

# 		print  tofind
# 		newcolors = []

# 		if allcolors:
# 			for color in allcolors:
# 				if color[1][3] > 0:
# 					for x in xrange(1,color[0]):
						
# 						newcolors.append((color[1][0], color[1][1], color[1][2], color[1][3]))
# 			avgcolor = tuple(map(lambda y: round(sum(y) / float(len(y))/255, 3), zip(*newcolors)))
# 			avgnormal = avgcolor[0:3]
# 			avgalpha = avgcolor[3]
# 			if avgalpha > 0.5:
# 				avgalpha = 1
# 			material = Material(blockid=tofind,color=avgnormal,name=name,alpha = avgalpha, blandname=name)
# 		else:
# 			material = Material(blockid=tofind,name=name, blandname=name)

		
# 		materials.update({tofind:material.getDict()})

# materials.update( material.addRest(materials) )

# print "length of materials found on site: " + str(len(materials))

# matsandtex = {"materials":materials,"textures":textures}


# f.write(repr(matsandtex))