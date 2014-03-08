import random
lista = []
for i in range(10):
	lista.append(random.randint(1,100))
lista.sort()
print('Maior número: %d / Menor número: %d' %(lista[0],lista[9]))
	
