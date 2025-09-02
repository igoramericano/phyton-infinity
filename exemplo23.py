n = int(input('Digite um número: '))

soma = 0
numero = 1

while numero <= n:
    soma += numero
    numero += 1

print(f'A soma de 1 a {n} é: {soma}')