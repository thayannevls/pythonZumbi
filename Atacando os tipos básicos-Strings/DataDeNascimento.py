meses = [ 'Janeiro', 'Fervereiro', 'Março', 'Abril','Maio','Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
data = input ('Digite sua data de nascimento: ').split('/')
dia = int(data[0])
mes = int(data[1])
ano = int(data[2])
print ( '%d de %s de %d' %(dia, meses[ mes - 1], ano))
