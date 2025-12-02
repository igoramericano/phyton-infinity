a = [2,3,4,7]
b = a
b[2] = 8

print(f'Lista a: {a}')
print(f'Lista b: {b}')

print('As listas se igualam porque o código foi definido como b=a fora de um loop, então ambas as variáveis apontam para o mesmo local na memória.')