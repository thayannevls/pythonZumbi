def fat(n): #Número fatorial
	a = 1 
	while n > 0:
		a = a * n #fatorial
		n = n - 1 #diminuindo até 0
	return a
for i in range(5): 
	print(fat(i))


	
	
