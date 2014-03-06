#fatorial de n
i = 1 #contador
fat = 1 #acumulador
n= int(input('Digite um número:')) #
while i <= n:
	fat = fat * i
	i = i + 1
print('fatorial de %d : %d' %(n,fat))
