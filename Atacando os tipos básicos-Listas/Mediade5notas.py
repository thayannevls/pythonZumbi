notas = [7.5,          #determinando a lista de notas
         6.0,
         10.0,
         7.5,
         6.5]
soma = 0          #acumulador da soma das notas
x = 0             #acumulador dos lugares da nota
while x < 5 :            #condição para somar o conteúdo da lista
	soma += notas[x]        #soma das notas
	x += 1                   #posição das notas
print( 'Média: %5.1f' %(soma / x) ) #imprimindo médica, soma das notas divido pelo número de notas(5)

  
