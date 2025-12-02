from random import randint
computador = randint(0, 5) #sorteia numero entre 0 e 5
print('-=-'*20)
print('Vou pensar num número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
player = int(input('Em que número pensei?: '))
print('PROCESSANDO...')

if player == computador:
    print('O número gerado foi {}, você acertou!' .format(computador))
else: print('O computador gerou {} e você inseriu {}, tente novamente!' .format(computador, player))
print('-=-'*20)
print('FIM')
print('-=-'*20)
