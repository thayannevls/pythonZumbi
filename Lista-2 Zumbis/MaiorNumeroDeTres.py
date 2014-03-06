#Verificar qual e o mais o numero
numero1 = int(input('Digite o primeiro número:'))
numero2 = int(input('Digite o segundo número:'))
numero3 = int(input('Digite o terceiro número:'))
#verificando os numeros abaixo
if numero1 >= numero2 and numero1 >= numero3: #verificando se o numero1 é o maior, 
	print('O primeiro número, %d, é o maior!' %numero1)
elif numero2 >= numero3:
	print('O segundo número, %d, é o maior!' %numero2)
else:
	print('O terceiro número, %d, é o maior!' %numero3)
