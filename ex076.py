#aqui começa o MODULO 3, tuplas.
#tuplas() são imutáveis.
#dicionários{} e listas[] são mutáveis.
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')
print('-' * 30)
print('HORA DA LARICA!')
print('-' * 30)
print(lanche[0]) #FORMA 1
print(lanche[1])
print(lanche[2])
print(lanche[3])
print(lanche[4])
print('-' * 30)
for cont in range(0, len(lanche)): #FORMA 2
    print(lanche[cont])

for comida in lanche:               #FORMA 3
    print(f'Eu vou comer {comida}') 
print('Comi pra caramba!')
print('-' * 30)
print(sorted(lanche)) #ordena em ordem alfabética
print('"print sorted" ordena em ordem alfabética')
print('-' * 30)
