from __future__ import division

from libPoint import Point_C


def prodDist(point1,i,listePoint):
	j=0	
	produit=1
	while j<len(listePoint):
		if j!=i:
			produit = produit * point1.distance(listePoint[j])**listePoint[j].mu
		j+=1
	return produit



def poids(point1,i,listePoint):
	j=0
	numerateur = prodDist(point1,i,listePoint)
	denominateur=0
	while j<len(listePoint):
		denominateur+=prodDist(point1,j,listePoint)
		j+=1
	return numerateur/denominateur
	
	
def shepard(point,listePoint):
	listePoint= [pointIt for pointIt in listePoint if pointIt.val!=None]
	i=0
	somme=0;
	while i<len(listePoint):
		somme+=poids(point,i,listePoint)*listePoint[i].val
		i+=1
		
	print "shepard:({},{}):{}".format(point.x,point.y,somme)
	return somme

	
if __name__ == '__main__':

	
	point1 = Point_C(0,0,1)
	print "point1:{}".format(point1)
	point2 = Point_C(0,1,2)
	print "point2:{}".format(point2)
	point3 = Point_C(1,0,3)
	print "point3:{}".format(point3)
	point4 = Point_C(1,1,4)
	print "point4:{}".format(point4)
	
	data = list()
	data.append(point1)
	data.append(point2)
	data.append(point3)
	data.append(point4)
	
	print "data:{}".format(data)
	
	interest = Point_C(0.5,0.5,2)
	
	print "interest:{}".format(interest)

	print "shepard(interest,data):{}".format(shepard(interest,data))
		
