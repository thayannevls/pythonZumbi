M= float(input('Preço da mercadoria:'))
D= float(input('Percentual do desconto:'))
Desconto= M*D/100
Preco = M-Desconto
print(' Seu desconto foi de R$ %.2f .' %Desconto)
print ('O novo preço do produto é R$ %.2f.' %Preco)
 
