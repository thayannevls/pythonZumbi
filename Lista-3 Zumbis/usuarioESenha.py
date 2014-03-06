print('O usuário e a senha não podem ser iguais.')
while True:
	usuario = input('Digite seu usuário:')
	senha = input('Digite sua senha:')
	if usuario != senha:
		break
	print('São iguais, tente de novo.')
print('Pronto.')
