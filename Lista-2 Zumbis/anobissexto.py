#verificar se um ano é bissexto
ano = int(input('Digite um ano:')) #ano a ser conferido, determinado pelo usuario
#condicoes para ser bissexto ou nao, abaixo.
if (ano % 4 == 0) and ( ano % 100 != 0 or ano % 400 == 0): #se for
	print('O ano é bissexto')
else: #se na for
	print('Não é bissexto') 
#output
