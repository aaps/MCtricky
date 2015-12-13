#!/usr/bin/python -B

from points import *

class Material:

	def __init__(self, emittance=None, color=None, alpha=None, blockid=None, name=None, uvs=None, textures=None, model=None ):
		
		self.setTexture(textures)

		self.setUvs(uvs)

		self.setEmitance(emittance)

		self.setColor(color)

		self.setAlpha(alpha)

		self.setName(name)

		self.setModel(model)


	def getDict(self):
		thedict = {"emittance":self.emittance,"alpha":self.alpha,"name":self.name,"uvs":self.uvs,"color":self.color, "textures":self.textures,"model":self.model.totuplelist()}
		return thedict

	def setModel(self, model=None):
		self.model = PointList()
		self.model.append([Point3D(-0.5,0.5,-0.5),Point3D(0.5,0.5,-0.5),Point3D(0.5,-0.5,-0.5),Point3D(-0.5,-0.5,-0.5)])
		self.model.append([Point3D(-0.5,0.5,0.5),Point3D(0.5,0.5,0.5),Point3D(0.5,-0.5,0.5),Point3D(-0.5,-0.5,0.5)])
		self.model.append([Point3D(-0.5,-0.5,0.5),Point3D(-0.5,-0.5,-0.5),Point3D(0.5,-0.5,-0.5),Point3D(0.5,-0.5,0.5)])
		self.model.append([Point3D(-0.5,0.5,0.5),Point3D(-0.5,0.5,-0.5),Point3D(0.5,0.5,-0.5),Point3D(0.5,0.5,0.5)])
		self.model.append([Point3D(-0.5,0.5,-0.5),Point3D(-0.5,-0.5,-0.5),Point3D(-0.5,-0.5,0.5),Point3D(-0.5,0.5,0.5)])
		self.model.append([Point3D(0.5,0.5,-0.5),Point3D(0.5,-0.5,-0.5),Point3D(0.5,-0.5,0.5),Point3D(0.5,0.5,0.5)])

		if model: 
			assert isinstance(model, list), "model should be list"
			self.model = model

	def setName(self, name=None):
		self.name = "Unknown"
		if name: 
			assert isinstance(name, str), "name should be string"
			self.name = name

	def setTexture(self,textures=None):
		self.textures = ()
		if textures:
			assert (textures is tuple), "Textures should be tuple"
			self.textures = textures

	def setUvs(self, uvs=None):
		self.uvs = ()
		if uvs:
			assert isinstance(uvs, tuple), "uvs should be tuple"
			self.uvs = uvs

	def setColor(self, color=None):
		self.color = (0,0,0)
		if color:
			assert isinstance(color, tuple), "Color should be tuple"
			self.color = color

	def setEmitance(self, emittance=None):
		self.emittance = 0
		if emittance:
			assert isinstance(emittance, (int, float)), "Emit value should be number"
			self.emittance = emittance

	def setAlpha(self, alpha=None):
		self.alpha = 0
		if alpha:
			assert isinstance(alpha, (int, float)), "Alpha should be number"
			self.alpha = alpha

	def setId(self, blockid=None):
		self.blockid = (0,0)
		if blockid:
			assert isinstance(blockid, tuple), "blockid should be tuple"
			self.blockid = blockid