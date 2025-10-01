import random
vitorias = 0
print('__'*30)
while True:
    print('VAMOS JOGAR PAR OU ÍMPAR')
    jogador = int(input('Digite um número entre 0 e 10: '))
    computador = random.randint(0, 11) #aleatório entre 0 e 10
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    if tipo == 'P': 
        if total % 2 == 0:
            resultado = 'PAR'
            print('Você VENCEU!')
            vitorias += 1
        else:
            resultado = 'ÍMPAR'
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 != 0: # Para ímpar, o resto da divisão por 2 deve ser diferente de 0.
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    print('__'*30)
    print(f'Você jogou {jogador} e o computador jogou {computador}.')
    print(f'O total {total} é {resultado}.')
    print('__'*30)
    