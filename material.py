#!/usr/bin/python -B

from shapes import *
from staticvalues import *
import ast
import os.path

class Material:

	def __init__(self, emittance=None, color=None,interneighbor=None,extraneighbor=None, alpha=None, blockid=None, name=None,blandname = None, uvs=None, textures=None, models=None ):
		
		self.shapemaker = Shapes()

		self.setId(blockid)

		self.setTexture(textures)

		self.setInterNeighbor(interneighbor)

		self.setExtraNeighbor(extraneighbor)

		self.setUvs(uvs)

		self.setEmitance(emittance)

		self.setColor(color)

		self.setAlpha(alpha)

		self.setName(name)

		self.setModel(models)

		self.setBlandName(blandname)

	def addRest(self, adict):
		diff = set(matstatics)-set(adict)
		tempdict = {}
		for item in diff:
			tempdict.update({item:matstatics[item]})
		return tempdict


	def getDict(self):
		thedict = {"emittance":self.emittance,"alpha":self.alpha,"name":self.name,"uvs":self.uvs,"color":self.color, "textures":self.textures,"models":self.models, "blandname":self.blandname, "interneighbor":self.interneighbor, "extraneighbor":self.extraneighbor}
		return thedict

	def setBlandName(self, blandname=None):
		self.blandname = "unknown"
		if blandname:
			assert isinstance(blandname, str), "blandname should be string"
			self.blandname = blandname.lower().replace(" ", "_")
		elif self.blockid in matstatics:
			self.blandname = matstatics[self.blockid]['blandname']

	def setInterNeighbor(self, interneighbor=None):
		self.interneighbor = False
		if interneighbor:
			assert isinstance(interneighbor, bool), "interneighbor should be Boolean"
			self.interneighbor = interneighbor
		elif self.blockid in matstatics:
			
			self.interneighbor = matstatics[self.blockid]['interneighbor']

	def setExtraNeighbor(self, extraneighbor=None):
		self.extraneighbor = False
		if extraneighbor:
			assert isinstance(extraneighbor, bool), "extraneighbor should be Boolean"
			self.extraneighbor = extraneighbor
		elif self.blockid in matstatics:
			
			self.extraneighbor = matstatics[self.blockid]['extraneighbor']

	def setModel(self, models=None):
		if not hasattr(self, 'models'):
			self.models = []

		if models:
			assert isinstance(models, List), "models should be list"
			
			self.models = models
		elif self.blockid in matstatics:
			for model in matstatics[self.blockid]['models']:
				if os.path.exists(modellocation + model +  '.mcmd'):
					modelfile = open(modellocation + model +  '.mcmd', 'r')
					modelstring = modelfile.read()
					self.models.append(ast.literal_eval(modelstring))
					modelfile.close()
					
				else:
					self.models.append( self.shapemaker.makeblockshape().totuplelist())
		else:
			
			self.models.append( self.shapemaker.makeblockshape().totuplelist())

	def setName(self, name=None):
		self.name = "Unknown"
		if name:
			assert isinstance(name, str), "name should be string"
			self.name = name
		elif self.blockid in matstatics:
			self.name = matstatics[self.blockid]['name']

	def setTexture(self,textures=None):
		self.textures = []
		if textures:
			assert (textures is list), "Textures should be tuple"
			self.textures = textures
		elif self.blockid in matstatics:
			self.textures = matstatics[self.blockid]['textures']


	def setUvs(self, uvs=None):
		self.uvs = []
		if uvs:
			assert isinstance(uvs, list), "uvs should be tuple"
			self.uvs = uvs
		elif self.blockid in matstatics:
			self.uvs = matstatics[self.blockid]['uvs']

	def setColor(self, color=None):
		self.color = (0,0,0)
		if color:
			assert isinstance(color, tuple), "Color should be tuple"
			self.color = color
		elif self.blockid in matstatics:
			self.color = matstatics[self.blockid]['color']

	def setEmitance(self, emittance=None):
		self.emittance = 0
		if emittance:
			assert isinstance(emittance, (int, float)), "Emit value should be number"
			self.emittance = emittance
		elif self.blockid in matstatics:
			self.emittance = matstatics[self.blockid]['emittance']

	def setAlpha(self, alpha=None):
		
		self.alpha = 0
		if alpha:
			assert isinstance(alpha, (int, float)), "Alpha should be number"
			self.alpha = alpha
		elif self.blockid in matstatics:
			self.alpha = matstatics[self.blockid]['alpha']

	def setId(self, blockid=None):
		self.blockid = (0,0)
		if blockid:
			assert isinstance(blockid, tuple), "blockid should be tuple"
			self.blockid = blockid