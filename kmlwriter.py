from lxml import etree
from pykml.factory import KML_ElementMaker as KML

indicePression = 2
indiceAltitude = 4
indiceLatitude = 5
indiceLongitude = 6


def initDocument():
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
	return doc

def addStations(doc,stations):
	for value in stations.itervalues():
		pm1 = KML.Placemark(
			KML.name(value[1]+"-"+value[0]),
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


def writeRow(doc,row):
	pass

def writeFile(file,doc):
	with open(file,'w') as out:
		out.write(etree.tostring(doc,pretty_print=True))
	