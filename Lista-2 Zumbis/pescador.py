#verificar se o peso passou do limite, e calcular  a multa
peso = float(input('Peso:')) #peso dado pelo usuario
if (peso > 50 #condicao do peso, passou do limite
	excesso = peso - 50 #calcula o excesso
	print ('Excesso: %.1f quilos' %excesso)
	multa  = excesso * 4.00 #calcular a multa, 4 reais por quilo
	print('Multa: R$ %.2f' %multa)
else: #se nao passar do limite
	print('0')
	
