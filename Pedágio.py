import math
distancia=float(input('Digite a distância da sua viagem em Km:'))
c1=  distancia * 0.5
c2=  distancia * 0.45
print('Vamos calcular o valor a ser pago!')
if distancia <= 200:
    print('O valor a ser pago é {} reais'.format(c1))
else:
    print('O valor a ser pago é {} reais'.format(c2))
