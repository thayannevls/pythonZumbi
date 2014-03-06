vetor = []
contador = 1
while contador <= 4:
	notas = float(input('Digite a %d nota: ' %contador))
	vetor.append(notas)
	contador += 1
print(vetor)
x = 0
soma = 0
while x <= 3:
	soma += vetor[x]
	x += 1
print ('Média: %5.2f' %(soma/4))
	
	
