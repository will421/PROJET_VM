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
				id="truc"
			),
			KML.Style(
				KML.LineStyle(
					KML.color("ff0000ff"),
					KML.width(1)
				),
				KML.PolyStyle(
					KML.color("ffff0000")
				),
				id="redLineBluePoly"
			)
		)
	)
	return doc

def addStations(doc,stations):
	for value in stations.itervalues():
		pm1 = KML.Placemark(
			#KML.name(value[]+"-"+value[0]),
			KML.name(value[2]),
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
		
def addStations2(doc,points):
	for value in points:
		pm1 = KML.Placemark(
			#KML.name(value[]+"-"+value[0]),
			KML.name(value.val),
			KML.Point(
				KML.altitudeMode("relativeToGround"),
				KML.description(str(value)),
				KML.coordinates("{},{},{}".format(
					value.x,
					value.y,
					1000,
				)
				),
			),
		)
		doc.Document.append(pm1)

def addSegment(doc,seg,colorStr):
	pm1 = KML.Placemark(
		KML.name("OneSegment"),
		KML.visibility(1),
		#KML.styleUrl("#redLineBluePoly"),
		KML.Style(
			KML.LineStyle(
				KML.color(colorStr),
				KML.width(3)
			)
		),
		KML.LineString(
			KML.extrude(1),
			KML.tesselate(0),
			#KML.altitudeMode("relativeToGround"),
			KML.coordinates("{}\n{}".format(seg[0].toKMLstr(),seg[1].toKMLstr())
			)
		)
	)
	doc.Document.append(pm1)

def addLine(doc,line):
	coordinates = "";
	for p in line:
		coordinates += ("\n" + p.toKMLstr())
	pm1 = KML.Placemark(
		KML.name("GridLine"),
		KML.visibility(1),
		KML.LineString(
			KML.extrude(1),
			#KML.altitudeMode("relativeToGround"),
			KML.tesselate(0),
			KML.coordinates(coordinates)
		)
	)
	doc.Document.append(pm1)


def addIso(doc,line,colorStr):
	for seg in line:
		addSegment(doc,seg,colorStr)
		
def addGrille(doc,grille):
	for i in range(0,len(grille)):
			addLine(doc,grille[i])
			line = [p[i] for p in grille]
			addLine(doc,line)

def writeFile(file,doc):
	with open(file,'w') as out:
		out.write(etree.tostring(doc,pretty_print=True))
	