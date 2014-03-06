n = int(input('Digite um número:'))
i = 1
while (i * ( i + 1) * (i + 2) < n):
	i = i + 1
if (i* ( i + 1 ) * ( i + 2 ) == n) :
	print('%d é triângular!' %n)
else:
	print(' %d não é triângular!'%n)
	
	
