def embaralha(t):
	import random
	lista = list(t)
	random.shuffle(lista)
	return ''.join(lista)
i = 'bananas'
print(embaralha(i))

