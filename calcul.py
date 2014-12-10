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
	j=1
	numerateur = prodDist(point1,i,listePoint)
	denominateur=0
	while j<len(listePoint):
		denominateur+=prodDist(point1,j,listePoint)
		j+=1
	return numerateur/denominateur
	
	
def shepard(point,listePoint):
	i=0
	somme=0;
	while i<len(listePoint):
		somme+=poids(point,i,listePoint)
		i+=1
	return somme

	
if __name__ == '__main__':
	print "ca marche ?"
	data = list()
	data.append(Point_C(1,1,1))
	data.append(Point_C(2,2,2))
	data.append(Point_C(3,3,3))
	data.append(Point_C(4,4,4))
	data.append(Point_C(5,5,5))
	data.append(Point_C(6,6,6))
	
	interest = Point_C(7,7,3)
	
	print shepard(interest,data)
		
