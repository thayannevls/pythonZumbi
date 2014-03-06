#condicao de existencia de um triangulo, e classifica-lo
lado1 = int(input('Digite o primeiro lado do triângulo:'))
lado2 = int(input('Digite o segundo lado do triângulo:'))
lado3 = int(input('Digite o terceiro lado do triângulo:'))
if (lado1 < lado2 + lado3): #condicao que determina se é triangulo ou não
	print('É um triângulo!')
#abaixo verifica o tipo do triangulo com as condicoes do if
	if (lado1 == lado2 == lado3):
		print('Tipo: Triângulo equilátero.')
	elif (lado1 != lado2 != lado3):
		print('Tipo: Triângulo escaleno.')
	else:
		print('Tipo:Triângulo isósceles.')
else: #se nao for triangulo
	print('Não é um triângulo!')
