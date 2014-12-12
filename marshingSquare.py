import sys
import coordinateGrille as Grille


def processAmbiguous(square,value):
	valMid = (square[0][0].val+square[0][1].val+square[1][0].val+square[1][1].val)/4
	p0 = processCoeff(square,0,value)
	p1 = processCoeff(square,1,value)
	p2 = processCoeff(square,2,value)
	p3 = processCoeff(square,3,value)
	if valMid<value:
		if square[0][0]<value:
			return [(p3,p2),(p0,p1)]
		else :
			return [(p0,p3),(p1,p2)]
	else :
		if square[0][0]<value:
			return [(p0,p3),(p1,p2)]
		else :
			return [(p3,p2),(p0,p1)]
			
def processCoeff(square,edge,value):
	if edge == 0 :
		return (grille[0][0]+grille[0][1])*0.5
	if edge ==1 :
		return (grille[0][1]+grille[1][1])*0.5
	if edge ==2 :
		return (grille[1][1]+grille[1][0])*0.5
	if edge ==3 :
		return (grille[1][1]+grille[1][0])*0.5
	raise Exception("What?")

def processSquare(square,value):
	code = 0;

	if square[0][1] > value:
		code = code | 1
	if square[1][1] > value:
		code = code | 2
	if square[1][0] > value:
		code = code | 4
	if square[0][0] > value:
		code = code | 8

	if code==0 || ~code==0:
		return res
	if code==1 || 15-code==1:
		p1 = processCoeff(square,0,value)
		p2 = processCoeff(square,1,value)
		return [(p1,p2)]
	if code==2 || 15-code==2:
		p1 = processCoeff(square,1,value)
		p2 = processCoeff(square,2,value)
		return [(p1,p2)]
	if code==3 || 15-code==3:
		p1 = processCoeff(square,0,value)
		p2 = processCoeff(square,2,value)
		return [(p1,p2)]
	if code==4 || 15-code==4:
		p1 = processCoeff(square,2,value)
		p2 = processCoeff(square,3,value)
		return [(p1,p2)]
	if code==5 || 15-code==5:
		return processAmbiguous(square,value)
		
	if code==6 || 15-code==6:
		p1 = processCoeff(square,1,value)
		p2 = processCoeff(square,3,value)
		return [(p1,p2)]
	if code==7 || 15-code==7:
		p1 = processCoeff(square,0,value)
		p2 = processCoeff(square,3,value)
		return [(p1,p2])]
	

def main(argv):
	
	value = 5
	grille = Grille.generate()
	nbSquare = len(grille)-1;
	
	var res = []
	
	for j in range(0,nbSquare):
		for i in range(0,nbSquare):
			square = [[0] * 2 for _ in range(2)]
			square[0][0] = grille[coordX][coordY]
			square[0][1] = grille[coordX][coordY+1]
			square[1][0] = grille[coordX+1][coordY]
			square[1][1] = grille[coordX][coordY+1]
			res = res + processSquare(square,value)
		
		
	print res

if __name__ == '__main__':
	main(sys.argv[1:])