#input do usuário
min=int(input('Minutos utilizados:'))
#Irá verificar o preco por minuto de acordo com os minutos utiziliados
if min<200:
	preco=0.20
elif min<=400:
	preco=0.18
elif min<=800:
	preco=0.15
else: #Se ultrapassar 800
	print('Parabéns, você utilizou mais que 800 minutos e ganhou uma promoção.')
	preco=0.8
print('Sua conta foi de R$ %.2f' %(min*preco))
#output

