# Aula 17 LISTAS - Parte 1

#listas são mutáveis 

#criando uma lista

num = [2, 5, 9, 1, 10, 25]

num.pop() #remove o último elemento da lista
num.remove(5) #remove o primeiro elemento 5 da lista
num.append(7) #adiciona o elemento 7 no final da lista
num.sort() #ordena a lista em ordem crescente

if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos') #mostra a quantidade de elementos


#outra forma de criar uma lista
valores = list(range(0, 26)) #cria uma lista com valores de 0 a 25
valores.sort(reverse=True) #ordena a lista em ordem decrescente
print(valores)
for numeros in valores:
    print(f'\n Essa lista tem {len(valores)} elementos', end='')
    break
    
    