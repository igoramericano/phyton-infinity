matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('-' * 30)
print('INSIRA VALORES LINHA | COLUNA')
print('-' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
print('-' * 30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]}]', end='') 
    print()