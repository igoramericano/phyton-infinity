def leiaInt(msg):
    while True:
        try:
            n = int(input(msg)) 
        except (ValueError, TypeError):
            print('\033[31mDigite um número inteiro válido \033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg)) 
        except (ValueError, TypeError):
            print('\033[31mDigite um número inteiro válido \033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n
        
n1 = leiaInt('Digite um inteiro: ')
n2 = leiaFloat('Digite um Real: ')
c = n1/n2
print(f'O valor inteiro foi {n1} e o Real foi {n2}')
print(f'A divisão entre eles foi de {c:.2f}')