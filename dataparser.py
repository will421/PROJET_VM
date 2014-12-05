# -*- coding: utf-8 -*-
import csv
import sys
from lxml import etree
from pykml.factory import KML_ElementMaker as KML

indicePression = 2
indiceAltitude = 4
indiceLatitude = 5
indiceLongitude = 6


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
			writeRow(row)
	
def writeRow(row):
	pass

	
def addStations(doc,stations):
	for value in stations.itervalues():
		pm1 = KML.Placemark(
			KML.name(value[0]),
			KML.Point(
				KML.altitudeMode("relativeToGround"),
				KML.description(str(value)),
				KML.coordinates("{},{},{}".format(
					value[indiceLongitude],
					value[indiceLatitude],
					value[indiceAltitude],
				)
				),
			),
		)
		doc.Document.append(pm1)

def main(argv):
	stations = loadStations("stations.csv")
	doc = KML.kml(
		KML.Document(
			KML.Name("Sun Position"),
			KML.Style(
				KML.IconStyle(
					KML.scale(1.2),
					KML.Icon(
						KML.href("http://maps.google.com/mapfiles/kml/shapes/shaded_dot.png")
					),
				),
				id="truc",
			)
		)
	)
	addStations(doc,stations)
	
	data = loadData("data.csv")
			
	
	with open("out.kml","w") as out:
		out.write(etree.tostring(doc,pretty_print=True))


if __name__ == '__main__':
	main(sys.argv[1:])