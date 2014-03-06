V= int(input('Velocidade do carro:'))
M= float((V-110)*5)
if V>110:
	print('Você foi multado. E o valor a ser pago é R$ %.2f' %M)
if V <=110:
	print('Você está no limite, pode continuar!')
	
