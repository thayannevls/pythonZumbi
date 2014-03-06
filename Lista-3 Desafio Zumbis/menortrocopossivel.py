conta = float(input('Valor da conta:')) #determinando o valor da conta
pagamento = float(input('Valor pago:')) #determinando o valor pago
troco = pagamento - conta #calculando valor do troco
print ('O troco é de R$ %5.2f' %troco)
#verificar abaixo as notas que podem ser utilizadas
if troco >= 50: #se o troco poder ser pago com valores maior de 50
	if troco % 50 == 0: #se poder ser dado pela maior nota
		cedulas50 = troco / 50 #contando as cedulas
		print(' %d cédulas de 50 reais' %cedulas50)
	else:
		cedulas50 = int( troco / 50) #quantas cedulas de 50 dará
		resto = troco - (cedulas50 * 50) #resto que sobrará depois que pagar com as de 50
		if resto > 10:
			
