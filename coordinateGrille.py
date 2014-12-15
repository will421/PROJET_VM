import sys


coordNW =(51,-5)
coordNE =(51,10)
coordSW =(40,-5)
coordSE =(40,10)
nbDivV = 1
nbDivH = nbDivV


def pretty_print(grille):
	s = [[str(e) for e in row] for row in grille]
	lens = [max(map(len, col)) for col in zip(*s)]
	fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
	table = [fmt.format(*row) for row in s]
	print '\n'.join(table)



def main(argv):
	pass










if __name__ == '__main__':
	main(sys.argv[1:])