#!/usr/bin/python -B

from shapes import *

shapemaker = Shapes()

matstatics = {}
# everything can be downloaded from the web except the model, textures emittance and uvs

matstatics.update({(1,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0),"niceneighbor":False}})


matstatics.update({(2,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,1,0),"niceneighbor":False }})
matstatics.update({(3,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,1,0),"niceneighbor":False }})


matstatics.update({(30,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makexblock().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,1,0) ,"niceneighbor":True}})
matstatics.update({(31,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makexblock().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,1,0) ,"niceneighbor":True}})
matstatics.update({(31,1):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makexblock().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,1,0) ,"niceneighbor":True}})
matstatics.update({(31,2):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makexblock().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,1,0) ,"niceneighbor":True}})
matstatics.update({(31,3):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makexblock().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,1,0) ,"niceneighbor":True}})


matstatics.update({(8,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0),"niceneighbor":False}})
matstatics.update({(9,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})

matstatics.update({(20,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})

matstatics.update({(44,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makehalfblocks().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(44,1):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makehalfblocks().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(44,2):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makehalfblocks().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(44,3):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makehalfblocks().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(44,4):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makehalfblocks().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(44,5):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makehalfblocks().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(44,6):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makehalfblocks().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(44,7):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makehalfblocks().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})

matstatics.update({(43,8):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"QQ","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(43,9):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"WW","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(43,10):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"GG","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(43,11):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"BB","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(43,12):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"NN","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(43,13):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"RR","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(43,14):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"EE","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(43,15):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"OP","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})

matstatics.update({(53,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makenormalstairs().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(67,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makenormalstairs().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})

matstatics.update({(85,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":True}})


matstatics.update({(108,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makenormalstairs().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(109,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makenormalstairs().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})

matstatics.update({(113,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":True}})

matstatics.update({(114,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makenormalstairs().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(134,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makenormalstairs().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(135,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makenormalstairs().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(136,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makenormalstairs().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(156,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makenormalstairs().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(163,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makenormalstairs().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(164,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makenormalstairs().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(180,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makenormalstairs().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})

matstatics.update({(65,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeladdershapes().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(106,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeladdershapes().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})


matstatics.update({(79,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})

matstatics.update({(95,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(95,1):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(95,2):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(95,3):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(95,4):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(95,5):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(95,6):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(95,7):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(95,8):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(95,9):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(95,10):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(95,11):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(95,12):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(95,13):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(95,14):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(95,15):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})

matstatics.update({(101,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":True}})

matstatics.update({(102,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})

matstatics.update({(160,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(160,1):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(160,2):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(160,3):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(160,4):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(160,5):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(160,6):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(160,7):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(160,8):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(160,9):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(160,10):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(160,11):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(160,12):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(160,13):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(160,14):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})
matstatics.update({(160,15):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})

matstatics.update({(174,0):{"emittance":0,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0) ,"niceneighbor":False}})

matstatics.update({(50,0):{"emittance":5,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0),"niceneighbor":False}})

matstatics.update({(119,0):{"emittance":5,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0),"niceneighbor":False}})

matstatics.update({(51,0):{"emittance":5,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0),"niceneighbor":False}})

matstatics.update({(91,0):{"emittance":5,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0),"niceneighbor":False}})

matstatics.update({(10,0):{"emittance":5,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0),"niceneighbor":False}})

matstatics.update({(11,0):{"emittance":5,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0),"niceneighbor":False}})

matstatics.update({(169,0):{"emittance":5,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0),"niceneighbor":False}})

matstatics.update({(62,0):{"emittance":5,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0),"niceneighbor":False}})

matstatics.update({(246,0):{"emittance":5,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0),"niceneighbor":False}})

matstatics.update({(90,0):{"emittance":5,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0),"niceneighbor":False}})

matstatics.update({(130,0):{"emittance":5,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0),"niceneighbor":False}})

matstatics.update({(379,0):{"emittance":5,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0),"niceneighbor":False}})

matstatics.update({(39,0):{"emittance":5,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0),"niceneighbor":False}})

matstatics.update({(122,0):{"emittance":5,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0),"niceneighbor":False}})

matstatics.update({(120,0):{"emittance":5,"uvs":[], "textures":[], "model":shapemaker.makeblockshape().totuplelist(), "blandname":"" ,"name":"","alpha":1, "color":(0,0,0),"niceneighbor":False}})