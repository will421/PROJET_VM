from __future__ import division
import sys
import coordinateGrille as Grille
from libPoint import *
import dataparser as Parser
import kmlwriter as Writer
import numpy as np

def processAmbiguous(square,value):
	valMid = (square[0][0].val+square[0][1].val+square[1][0].val+square[1][1].val)/4
	p0 = processCoeff(square,0,value)
	p1 = processCoeff(square,1,value)
	p2 = processCoeff(square,2,value)
	p3 = processCoeff(square,3,value)
	if valMid<value:
		if square[0][0]<value:
			return [(p3,p2),(p0,p1)]
		else :
			return [(p0,p3),(p1,p2)]
	else :
		if square[0][0]<value:
			return [(p0,p3),(p1,p2)]
		else :
			return [(p3,p2),(p0,p1)]
			
def processCoeff(square,edge,value):

	#print "Edge:{}".format(edge)

	if edge == 0: 
		p1=square[0][0]
		p2=square[1][0]
	elif edge ==1 :
		p1=square[1][0]
		p2=square[1][1]
	elif edge ==2 :
		p1=square[1][1]
		p2=square[0][1]
	elif edge ==3 :
		p1=square[0][1]
		p2=square[0][0]
	else :
		raise Exception("What?")
		
		
	alpha = (value-p1.val)/(p2.val-p1.val)
	#print "Alpha:{}".format(alpha)
	return (1-alpha)*p1+alpha*p2

def processSquare(square,value):
	code = 0;

	#print "square:" 
	#Grille.pretty_print(square)
	#print "value:{}".format(value)

	#import pdb; pdb.set_trace()
	if square[1][0].val > value:
		code = code | 1
	if square[1][1].val > value:
		code = code | 2
	if square[0][1].val > value:
		code = code | 4
	if square[0][0].val > value:
		code = code | 8

	#print "Cas:{}".format(code)
		
	if code==0 or 15-code==0:
		return []
	if code==1 or 15-code==1:
		p1 = processCoeff(square,0,value)
		p2 = processCoeff(square,1,value)
		return [(p1,p2)]
	if code==2 or 15-code==2:
		p1 = processCoeff(square,1,value)
		p2 = processCoeff(square,2,value)
		return [(p1,p2)]
	if code==3 or 15-code==3:
		p1 = processCoeff(square,0,value)
		p2 = processCoeff(square,2,value)
		return [(p1,p2)]
	if code==4 or 15-code==4:
		p1 = processCoeff(square,2,value)
		p2 = processCoeff(square,3,value)
		return [(p1,p2)]
	if code==5 or 15-code==5:
		return processAmbiguous(square,value)
		
	if code==6 or 15-code==6:
		p1 = processCoeff(square,1,value)
		p2 = processCoeff(square,3,value)
		return [(p1,p2)]
	if code==7 or 15-code==7:
		p1 = processCoeff(square,0,value)
		p2 = processCoeff(square,3,value)
		return [(p1,p2)]
	

def generate():
	size = 2
	grille = [[0] * size for _ in range(size)]
	grille[0][0] = Point_C(0,0,0)
	grille[0][1] = Point_C(0,1,0)
	grille[1][1] = Point_C(1,1,0)
	grille[1][0] = Point_C(1,0,1)

	return grille
def main(argv):
	
	index = 2
	nbDiv = 5
	nbIso = 5
	if len(argv)>0:
		nbDiv = int(argv[0])
	if len(argv)>1:
		index = int(argv[1])
	
	stations = Parser.loadStations("stations.csv")
	lPoints = Parser.loadPoints("data.csv",index,stations)

	doc = Writer.initDocument()
	Writer.addStations(doc,stations)
	
	grille = Grille.generateGrille(nbDiv,lPoints,index)
	Writer.addGrille(doc,grille)
	#import pdb; pdb.set_trace()
	minGrille = min([min(col,key=(lambda p: p.val)).val for col in grille])
	maxGrille = max([max(col,key=(lambda p: p.val)).val for col in grille])
	print "minG :{}, maxG :{}".format(minGrille,maxGrille)
	values = np.linspace(minGrille,maxGrille,10)
	#values = [101504.400,101504.500]
	#values = [101500,101499]
	for value in values:
		
		nbSquare = len(grille)-1;
		res = []
	
		for j in range(0,nbSquare):
			for i in range(0,nbSquare):
				square = [[0] * 2 for _ in range(2)]
				square[0][0] = grille[i][j]
				square[0][1] = grille[i][j+1]
				square[1][1] = grille[i+1][j+1]
				square[1][0] = grille[i+1][j]
				res = res + processSquare(square,value)
		print "NbSegment:{}".format(len(res))
		Writer.addIso(doc,res)
		
		
	Writer.writeFile("out.kml",doc)


if __name__ == '__main__':
	main(sys.argv[1:])
	
	

	