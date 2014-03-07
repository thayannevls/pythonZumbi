n = int(input('Digite um número:')) #posicao do numero fibonacci
a,b = 1,1 #primeiros numeros da sequencia
contador = 1
while k < n - 2: #condicao
	a,b = b, a + b #somando com o anteiror
	k += 1 #adicionando mais um ao contador
print('F(%d): %d' %(n,b))
