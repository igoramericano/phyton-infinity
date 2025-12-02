from random import randint
from time import sleep
def linha():
    print('-' * 30)
def maior(*num):
    cont = maior = 0
    print(f'Analizando os valores passados ')
    for valor in num:
        print(f'{valor}...', end='', flush=True)  #flush true para ter pausa na contagem
        sleep(0.3)
        if cont == 0:
            maior = valor
        elif valor > maior:
            maior = valor
        cont += 1
    linha()
    print(f'\n Foram informados {cont} valores')
    linha()
    print(f'\n O maior valor informado foi {maior}')
    
maior(0, 5, 6, 2, 10, 22, 7)