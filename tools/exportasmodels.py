#!/usr/bin/python -B

from shapes import *
import ast

shapemaker = Shapes()
models = {}
modeldirpath = '../models/'

models.update({"flatblock":shapemaker.makeflatblocks().totuplelist()})
models.update({"halfblock":shapemaker.makehalfblocks().totuplelist()})
models.update({"blockblock":shapemaker.makeblockshape().totuplelist()})
models.update({"xblock":shapemaker.makexblock().totuplelist()})

models.update({"stdstairs":shapemaker.makenormalstairs().totuplelist()})
models.update({"negstairs":shapemaker.makenegcornerstairs().totuplelist()})
models.update({"posstairs":shapemaker.makeposcornerstairs().totuplelist()})

models.update({"verflatblock":shapemaker.makeverticalflatblock().totuplelist()})
models.update({"stdfenceblock":shapemaker.makefenceshape().totuplelist()})
models.update({"plusblock":shapemaker.makeverticalplusblock().totuplelist()})

for model in models:

	f = open(modeldirpath + model +'.mcmo', 'w')
	f.write(repr(models[model]))
	f.close()