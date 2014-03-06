valor = float(input('Valor por hora:')) #descobrindo quanto ele ganha por horas
horas = int(input('Horas ao mês:')) #descobrindo quantas horas ele trabalha por mês
bruto = valor * horas #calculando o salario bruto
#abaixo calculando os descontos / valores de porcentagem dividos por 100
ir = bruto * 0.11
inss = bruto * 0.08
sindicato = bruto * 0.05
liquido = bruto - ir - inss - sindicato
print('+Salário bruto:  R$ %10.2f' %bruto)
print('-Ir: \t\t R$ %10.2f' %ir)
print('-INSS: \t\t R$ %10.2f' %inss)
print('-Sindicato: \t R$ %10.2f' %sindicato)
print('=Salário Liquido:R$ %10.2f' %liquido)
