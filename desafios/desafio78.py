lista = []
maior = menor = 0
for c in range (0,5):
    lista.append (int(input(f'Digite um valor para a posição {c}: ')))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('-='*30)
print(f'Você digitou os valores {lista}')
print('-='*30)
print(f'O maior valor digitado foi {maior} e o menor foi {menor}')
print('-='*30)
for i, v in enumerate (lista):
    if v == maior:
        print(f'O maior valor apareceu na posição {i}...')
    elif v == menor:
        print(f'O menor valor apareceu na posição {i}...')
    else:
        break
print('-='*30)