palavra = input('Digite uma palavra:')
n = 0
troca = ""
while n < len(palavra):
	if palavra[n] in "aeiou":
		troca = troca + "*"
	else:
		troca = troca + palavra[n]
	n += 1
print('Nova palavra %s' %troca)
