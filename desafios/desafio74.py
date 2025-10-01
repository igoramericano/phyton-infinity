import random

# Gera 4 valores aleatórios entre 1 e 100
lista = [valor1, valor2, valor3, valor4] = random.randint(1, 100)[0:4] 

print(f'Os valores sorteados foram: {lista}')
print(f'O maior valor sorteado foi: {max(lista)}') #max valor da lista
print(f'O menor valor sorteado foi: {min(lista)}') #min valor da lista