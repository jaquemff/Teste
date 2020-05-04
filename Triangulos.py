r1 = float(input('Digite o primeiro valor: '))
r2 = float(input('Digite o primeiro valor: '))
r3 = float(input('Digite o primeiro valor: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
	#print('Os valores PODEM formar um triângulo.')
	if r1 == r2 == r3:
		print('Equilátero.')
	elif r1 != r2 != r3 != r1:
		print('Escaleno.')
	else:
		print('Isósceles.')

else:
	print('Os valores NÃO PODEM formar um triângulo.')