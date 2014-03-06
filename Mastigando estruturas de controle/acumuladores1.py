#calcular a soma de dez numeros inteiros
n = 1 #determinando contador
soma = 0 #determinando acumulador
while n <= 10: #condicao para o contador
	x = int(input('Digite o %d número: ' %n)) #determinando a variavel x
	soma = soma + x
	n = n + 1
print('A média é %5.2f' %(soma/10))
