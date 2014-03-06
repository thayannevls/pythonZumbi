vetor = [] #determinando vetor
contador = 1 #contador
while contador <= 10: #condicao ate o numero 10
	n = float(input('Digite um número:')) #lendo valor
	vetor.append(n) #adiconando valor ao vetor
	contador += 1 #contando o numero de valores para parar
#abaixo imprimir na ordem inversa
contador = 9
while contador >= 0:
	print(vetor[contador])
	contador -= 1
