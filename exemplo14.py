# Pede ao usuário para digitar um número
numero = int(input('Digite um número inteiro: '))

# Usa o operador de módulo (%) para checar se o número é par
if (numero % 2) == 0:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é ímpar.')