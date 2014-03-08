import random
lista = []
while len(lista) < 15:
	t = random.randint(10,100)
	if t not in lista:
		lista.append(t)
print(lista)
	

