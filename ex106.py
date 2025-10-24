from time import sleep
c = ('\033[m',          # 0 - sem cores
     '\033[0;30;41m',  # 1 - vermelho
     '\033[0;30;42m',  # 2 - verde
     '\033[0;30;43m',  # 3 - amarelo
     '\033[0;30;44m',  # 4 - azul
     '\033[0;30;45m',  # 5 - roxo
     '\033[7;30m',     # 6 - branco
     '\033[0;30;47m',  # 7 - Fundo Branco
)

def ajuda(command):
    titulo(f'Acessando o manual do comando \'{command}\'', 7)
    print(c[6], end='')
    help(command)
    print(c[0], end='')
    sleep(2)


def titulo(msg, cor=0):
    tamanho = len(msg) + 4
    print(c[cor], end='')
    print('~' * tamanho)
    print(msg)
    print('~' * tamanho)
    print(c[0], end='')
    
comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYhelp 1.0', 2)
    comando = str(input('Função ou Biblioteca --> '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 7)
    