valordia= 60
valorkm= 0.15
dia= int(input('Insira a quantidade de dias que passou com o veículo: '))
km= int(input('Insira quantos km rodou com o carro: '))
total= (valordia * dia) + (valorkm * km)
print('-'* 12)
print('Tabela de preço')
print('Carro R$60/dia')
print('R$0.15 para cada km rodado')
print('Em {} dias, foi percorrido {}Km e o valor a pagar será de R${}' .format(dia,km,total))
