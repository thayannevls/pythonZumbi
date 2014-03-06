cidadeA = 80000 #NUMERO DE HABITANTES ATUAL DA CIDADE A
cidadeB = 200000 #NUMERO DE HABITANTES ATUAL DA CIDADE B
anos = 1 #CONTADOR DE ANOS
while cidadeA < cidadeB: #ENQUANTO O NUMERO DE HABITANTES DA CIDADE A FOR MENOR QUE B
	cidadeA = cidadeA + ((cidadeA * 3) / 100) #CALCULANDO O NUMERO DE HABITANTES DE A, ATÉ ULTRAPASSAR B
	cidadeB = cidadeB + ((cidadeB * 1.5) / 100) #CALCULANDO NUMERO DE HABITANTES DE ACORDO COM A TAXA DE CRESCIMENTO
	anos += 1 #ANOS
print('Em %d anos, a cidade A, ultrapassará a cidade B com %d habitantes e a cidade B estará com %d habitantes.' %(anos, cidadeA, cidadeB))
#output
	
