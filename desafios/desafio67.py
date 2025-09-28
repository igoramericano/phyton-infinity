n = int(input("Digite um número positivo para ver sua tabuada [ou 0 para SAIR]: "))

while n != 0:
    print(f'---Tabuada de {n}---')
    for i in range(1, 11): #aqui eu defino o intervalo a ser exibido
        print(f'{i} x {n} = {i * n}')
    print('----------------------')
    n = int(input('Digite outro número inteiro positivo [0 para SAIR]: '))
print('Programa encerrado.')