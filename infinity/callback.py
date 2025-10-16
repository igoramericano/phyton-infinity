def somar(a,b):
    somar = a + b
    return somar

def subtrair(a,b):
    subtrair =  a - b
    return subtrair
    
def multiplicar(a,b):
    multiplicar = a * b
    return multiplicar
    
def dividir(a,b):
    dividir = a/b
    return dividir

def executar_operação(a,b, operacao):
    return operacao

    if operacao == 1:
            somar(a,b)
            print(somar)
    elif operacao == 2:
            subtrair(a,b)
            print(subtrair)
    elif operacao == 3:
            multiplicar(a,b)
            print(multiplicar)
    elif operacao == 4:
            dividir(a,b)
            print(dividir)
    else:
        print('OPÇÂO INVALIDA, DIGITE de 1-4')
    a = int(input('Digite o valor de "a": '))
    b = int(input('Digite o valor de "b": '))