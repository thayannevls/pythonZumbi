print('Faça o que se pede e no final converteremos tudo para segundos.')
print('Ps.: Use apenas números.')
Dias = int(input('Dias:'))
Horas = int(input('Horas:'))
Minutos = int(input('Minutos:'))
Segundos = int(input('Segundos:'))

SD= Dias*3600
SH= Horas*3600
SM= Minutos*60
SS= Segundos*1

Resultado = SD+SH+SM+SS
print (Resultado, 'Segundos')

