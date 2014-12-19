import sys
import math
from libPoint import Point_C

coordNW =Point_C(51.0,-5.0)
coordNE =Point_C(51.0,10.0)
coordSW =Point_C(40.0,-5.0)
coordSE =Point_C(40.0,10.0)



def main(argv):
	generateGrille(1)


def generateGrille(nbDiv=1):
	
	nbPoints = int(math.pow((2+nbDiv),2))
	nbDivTotal = 2+ nbDiv

	grille= [[Point_C(0.0,0.0)] * nbDivTotal for _ in range(nbDivTotal)]
	
	arrayLong = generateArray(coordNW.y,coordNE.y,nbDiv,"long")
	arrayLat = generateArray(coordNW.x,coordSW.x,nbDiv,"lat")
	print(arrayLong)
	print(arrayLat)
	grille = completeGrille(grille,arrayLong,arrayLat,nbDiv)
	

def completeGrille(grille,arrayLong,arrayLat,nbDiv):
	for i in range (0,nbDiv+2):
		for j in range(0,nbDiv+2):
			grille[j][i] = Point_C(arrayLat[i],arrayLong[i])
	print(grille)
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