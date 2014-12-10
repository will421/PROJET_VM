# -*- coding: utf-8 -*-
import csv
import sys
from lxml import etree


from kmlwriter import *

doc = []

def loadStations(file):
	stations = {}
	with open(file,"r") as s:
		reader = csv.reader(s,delimiter=';')
		for row in reader:
			stations[row[0]] = row
	return stations

def loadData(file):
	data = []
	with open("data.csv","r") as f:
		reader= csv.reader(f,delimiter=';')
		for row in reader:
			writeRow(doc,row)


def main(argv):
	stations = loadStations("stations.csv")
	doc = initDocument()
	addStations(doc,stations)
	
	data = loadData("data.csv")
			
	writeFile("out.kml",doc)


if __name__ == '__main__':
	main(sys.argv[1:])