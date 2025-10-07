velocidade = float(input('Qual a velocidade atual do carro? '))
multa = (velocidade - 80) * 7
diferenca = velocidade - 80
if velocidade >= 88:
    print('MULTADO')
else:
    print('Dirija com segurança!')
print('{}Km/h acima do limite, você foi multado em R${:.2f}'.format(diferenca, multa))
print('-=-'*20)
print('FIM')
print('-=-'*20)
