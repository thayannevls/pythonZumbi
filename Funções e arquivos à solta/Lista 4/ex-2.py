import random
lista = []
par = []
impar = []
contador = 0
while contador < 20:
	lista.append(random.randint(1,100))
	if lista[contador] % 2 == 0:
		par.append(lista[contador])
	else:
		impar.append(lista[contador])
	contador += 1
print('Total: %s' %lista)
print('Pares: %s' %par)
print('Impares: %s' %impar)
