from __future__ import division
import math as m
class Point_C(object):
	'''
	love
	'''
	def __init__(self,L,l,val=-1,mu=1):
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

	def __mul__(self,val):
		if type(val) is int or type(val) is float :
			return Point_C(self.x*val,self.y*val,self.val,self.mu)
		else:
			raise NotImplementedError
			
	def __rmul__(self,val):
		return self.__mul__(val)
		
		
	def dist(self,p2):
		return self.distance(p2)
	
	def toKMLstr(self):
		return "{},{},{}".format(self.y,self.x,2000)
	
	def distance(self,p2):
		p=self.__sub__(p2)
		return m.sqrt((p.x)**2+(p.y)**2)
