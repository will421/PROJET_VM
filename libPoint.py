from __future__ import division
import math as m
class Point_C(object):
	'''
	rage
	'''
	def __init__(self,L,l,val,mu=1):
		self.x=L
		self.y=l
		self.val=val
		self.mu=mu
 
 
	def __repr__(self):
		return '('+str(self.x)+';'+str(self.y)+'):'+str(self.val)
					
	def __add__(self,val):
		if type(val) is Point_C :
			return Point_C(self.x+val.x,self.y+val.y,self.val,self.mu)
		else:
			raise TypeError
			
 
	def __sub__(self,val):
		if type(val) is Point_C :
			return Point_C(self.x-val.x,self.y-val.y,self.val,self.mu)
		else:
			raise TypeError
	def dist(self,p2):
		return self.distance(p2)
	
	def distance(self,p2):
		p=self.__sub__(p2)
		return m.sqrt((p.x)**2+(p.y)**2)
