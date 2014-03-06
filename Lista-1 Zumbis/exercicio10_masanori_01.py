Anos= int(input('Quantidade anos fumando:'))
Cigarros= int(input('Quantos cigarros fuma por dia:'))
#Regra de três: 144 cigarros=1 dia de vida
TCigarros= Anos*365*Cigarros
Dias_Perdidos= TCigarros/144
print('Você perdeu %d dias da sua vida, aproximadamente.' %Dias_Perdidos)

