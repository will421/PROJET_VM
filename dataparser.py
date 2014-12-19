# -*- coding: utf-8 -*-
import csv
import sys
from lxml import etree
from libPoint import *

from kmlwriter import indiceLongitude, indiceLatitude, initDocument, addStations, writeFile

doc = []

def loadStations(file):
	stations = {}
	with open(file,"r") as s:
		reader = csv.reader(s,delimiter=';')
		for i,row in enumerate(reader):
			if i==0: continue
			if len(row[0])>4: continue
			stations[float(row[0])] = row
	return stations

def loadPoints(file,indexValue,stations):
	points = []
	with open(file,"r") as f:
		reader= csv.reader(f,delimiter=';')
		for i,row in enumerate(reader):
			if i ==0: continue
			try:
				x = float(stations[float(row[0])][indiceLongitude])
				y = float(stations[float(row[0])][indiceLatitude])
			except KeyError:
				continue
			try :
				value = float(row[indexValue])
			except ValueError :
				value = None
				print "Warning, there is a wrong value in row {} for {}".format(i,indexValue) 
			points.append(Point_C(x,y,value))
		
	return points


def main(argv):
	stations = loadStations("stations.csv")
	doc = initDocument()
	addStations(doc,stations)
	
	data = loadPoints("data.csv",0,stations)

	writeFile("out.kml",doc)


if __name__ == '__main__':
	main(sys.argv[1:])