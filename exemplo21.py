import random

numero_secreto = random.randint(1, 100)

while True:
    try:
        chute = int(input('Adivinhe o número secreto (entre 1 e 100): '))
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")
        continue

    if chute == numero_secreto:
        print('Parabéns! Você acertou!')
        break
    else:
        print('Ops, você errou. Tente novamente!')

print('Fim do jogo.')