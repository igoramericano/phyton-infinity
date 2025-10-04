numeros = [[],[]] # numeros[0] = pares | numeros[1] = ímpares
valor = 0

for c in range(1,8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    elif valor % 2 != 0:
        numeros[1].append(valor)
numeros[0].sort() #variavel[posição da lista].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')