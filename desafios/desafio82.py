pares = []
impares = []
num = 0
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num != 999:
        if num % 2 == 0:
            pares.append(num)
        elif num % 2 != 0:
            impares.append(num)

print(f'Os números pares digitados foram: {pares}')
print(f'Os números ímpares digitados foram: {impares}')
 
 