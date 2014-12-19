from __future__ import division
import sys
import math
import os
from libPoint import Point_C
from calcul import shepard
import pickle

coordNW =Point_C(51.0,-5.0)
coordNE =Point_C(51.0,10.0)
coordSW =Point_C(41.0,-5.0)
coordSE =Point_C(41.0,10.0)



def pretty_print(grille):
	s = [[str(e) for e in row] for row in grille]
	lens = [max(map(len, col)) for col in zip(*s)]
	fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
	table = [fmt.format(*row) for row in s]
	print '\n'.join(table)



def main(argv):
	generateGrille(2)

def putInCache(nbDiv,grille,idCache):
	if nbDiv<6:
		return
	with open("cache/grille-{}-index{}".format(nbDiv,idCache),"wb") as f:
		pickle.dump(grille,f)



def checkInCache(nbDiv,idCache):
	if os.path.exists("cache/grille-{}-index{}".format(nbDiv,idCache)):
		with open("cache/grille-{}-index{}".format(nbDiv,idCache),"rb") as f:
			grille = pickle.load(f)
		return grille
	else :
		return None
	
def generateGrille(nbDiv=1,listePoint=None,idCache=None):
	print "Generating grille"
	grille = checkInCache(nbDiv,idCache)
	if grille != None:
		print "Grille loaded from cache"
		return grille
	
	
	nbPoints = int(math.pow((2+nbDiv),2))
	nbDivTotal = 2+ nbDiv

	grille= [[Point_C(0.0,0.0)] * nbDivTotal for _ in range(nbDivTotal)]
	
	arrayLong = generateArray(coordNW.y,coordNE.y,nbDiv,"long")
	arrayLat = generateArray(coordNW.x,coordSW.x,nbDiv,"lat")
	print "Array OK, now filling grille"
	#print(arrayLong)
	#print(arrayLat)
	grille = completeGrille(grille,arrayLong,arrayLat,nbDiv,listePoint)
	"Grille ready"
	putInCache(nbDiv,grille,idCache)
	return grille

def completeGrille(grille,arrayLong,arrayLat,nbDiv,listePoint):
	nbPoint = (nbDiv+2)**2
	k= 0
	for i in range (0,nbDiv+2):
		for j in range(0,nbDiv+2):
			if listePoint==None :
				grille[j][i] = Point_C(arrayLat[i],arrayLong[j])
			else :
				p = Point_C(arrayLat[i],arrayLong[j])
				#import pdb; pdb.set_trace()
				p.val = shepard(p,listePoint)
				grille[j][i] = p
			k += 1
			print '{:.2f}% of generation'.format((k/nbPoint)*100)
	#print(grille)
	return grille

def generateArray(deb,fin,nbDiv,type):

	deltaLongitude = abs(coordNW.y) + abs(coordNE.y)
	deltaLatitude = abs(coordNW.x) - abs(coordSW.x)
	arrayBuilt = [deb]

	if ( type == "lat"):
		
		for i in range (1,nbDiv+1):
			valDiv = 1 + nbDiv
			calc = deb - (deltaLatitude/valDiv)* i 
			arrayBuilt.append(calc)
		
		arrayBuilt.append(fin)
	
	elif (type =="long"):
		
		for i in range (1,nbDiv+1):
		
			valDiv = 1 + nbDiv
			
			calc = (deltaLongitude/valDiv)* i + deb
			arrayBuilt.append(calc)
		
		arrayBuilt.append(fin)
	return arrayBuilt


if __name__ == '__main__':
	main(sys.argv[1:])