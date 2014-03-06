#verificar qual é o menor número e o maior
#abaixo, determinando os numeros
numero1 = int(input('Digite o primeiro número:'))
numero2 = int(input('Digite o segundo número:'))
numero3 = int(input('Digite o terceiro número:'))
#abaixo, irá verificar o maior numero
if numero1 >= numero2 and numero1 >= numero3: #verificando se o maior numero é o primeiro
	print('O primeiro número é o maior(%d)' %numero1)
#verificando o menor, abaixo
	if numero2 < numero3:
		print('O segundo é o menor número(%d)' %numero2)
	else:
		print('O terceiro é o menor número(%d)' %numero3)
elif numero2 >= numero1 and numero2 >= numero3: #verificando se  o maior numero é o segundo
	print('O segundo número é o maior(%d)' %numero2)
#verificando o menor, abaixo
	if numero1 < numero3:
		print('O primeiro é o menor número(%d)' %numero1)
	else:
		print('O terceiro é o menor número(%d)' %numero3)
elif numero3 >= numero1 and numero3 >= numero2: #verificando se o maior número é o terceiro
	print('O terceiro número é o maior(%d)' %numero3)
#verificando o menor, abaixo
	if numero1 < numero2:
		print('O primeiro é o menor número(%d)' %numero1)
	else:
		print('O segundo é o menor número(%d)' %numero2)
#output
    


