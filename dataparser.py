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
			stations[float(row[0])] = row
	return stations

def loadPoints(file,indexValue,stations):
	points = []
	with open("data.csv","r") as f:
		reader= csv.reader(f,delimiter=';')
		for i,row in enumerate(reader):
			if i ==0: continue
			x = float(stations[float(row[0])][indiceLongitude])
			y = float(stations[float(row[0])][indiceLatitude])
			points.append(Point_C(x,y,float(row[indexValue])))
		
	return points


def main(argv):
	stations = loadStations("stations.csv")
	doc = initDocument()
	addStations(doc,stations)
	
	data = loadPoints("data.csv",0,stations)

	writeFile("out.kml",doc)


if __name__ == '__main__':
	main(sys.argv[1:])