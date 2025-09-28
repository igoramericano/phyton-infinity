valor = soma = total = 0
while valor != 999:
    valor = int(input('Digite um valor [P/ PARAR 999 ]: '))
    if valor != 999:
        soma += valor
        total += 1
print(f'Você digitou {total} números e a soma entre eles foi {soma}.')