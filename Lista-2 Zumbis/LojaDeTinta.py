metros = int(input('Área a ser pintada em metros quadrados:'))
if (metros % 54 == 0):
	latas = metros/54
	preco = latas * 80.00
	print('Quantidade de latas: %d / Preço: R$ %d,00' %(latas,preco))
else:
	latas = int(metros/54) + 1
	preco = latas * 80.00
	print('Quatidade de latas: %d / Preço: R$ %d,00' %(latas, preco))

	
	
