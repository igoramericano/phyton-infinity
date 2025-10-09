from time import sleep
def linha():
    print('-' * 30)
def mensagem(msg):
    linha()
    print(msg)
    linha()

def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')

    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont += p
        print('FIM!')

    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='', flush=True)
            sleep(0.5)
            cont -= p
        print(' F I M !')


# Programa principal
mensagem('CONTAGEM de 0 a 10 de 1 em 1')
contador(1, 10, 1)
mensagem('CONTAGEM de 10 a 0 de 1 em 2')
contador(10, 0, 2)
mensagem('Agora sua vez de contar: ')
inicio = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
passo = int(input('Digite o passo: '))
mensagem(f'Contando de {inicio} até {fim} de {passo} em {passo}')
contador(inicio, fim, passo)

print('         F I M        ')