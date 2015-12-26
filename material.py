#!/usr/bin/python -B

from shapes import *
from staticvalues import *

class Material:

	def __init__(self, emittance=None, color=None, alpha=None, blockid=None, name=None,blandname = None, uvs=None, textures=None, model=None ):
		
		self.shapemaker = Shapes()

		self.setId(blockid)

		self.setTexture(textures)

		self.setUvs(uvs)

		self.setEmitance(emittance)

		self.setColor(color)

		self.setAlpha(alpha)

		self.setName(name)

		self.setModel(model)

		self.setBlandName(blandname)


	def getDict(self):
		thedict = {"emittance":self.emittance,"alpha":self.alpha,"name":self.name,"uvs":self.uvs,"color":self.color, "textures":self.textures,"model":self.model, "blandname":self.blandname}
		return thedict

	def setBlandName(self, blandname=None):
		self.blandname = "unknown"
		if blandname:
			assert isinstance(blandname, str), "blandname should be string"
			self.blandname = blandname.lower().replace(" ", "_")
		elif self.blockid in matstatics:
			self.blandname = matstatics[self.blockid]['blandname']

	def setModel(self, model=None):
		self.model = self.shapemaker.makeblockshape().totuplelist()
		if model:
			assert isinstance(model, PointList), "model should be PointList"
			self.model = model
		elif self.blockid in matstatics:
			self.model = matstatics[self.blockid]['model']

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