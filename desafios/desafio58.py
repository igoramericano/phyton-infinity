import random
computador = random.randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('-' * 60)
print('Será que você consegue adivinhar qual foi?')
print('-' * 60)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Tente um valor mais alto...')
        elif jogador > computador:
            print('Tente um valor mais baixo...')
print('-' * 60)
print(f'Acertou! O número que eu pensei foi {computador}.')
print(f'Você precisou de {palpites} tentativas para me vencer.')
print('-' * 60)