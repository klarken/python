def granos():
	cont,trigot,suma,trigofinal = 0,1,0,0
	for x in range(1,64):
		trigot = (trigot * 2) + 1
		trigofinal = trigot -1
		trigot = trigofinal
		cont = cont +1
		suma = suma + trigot
		print"trigo",cont+1,trigot
		if(x==64-1):
			print "valor de la ultima casilla", trigot
	print "la suma total es"
	return suma +1
granos()
print granos()