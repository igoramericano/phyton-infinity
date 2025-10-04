galera = list()
dado = list()
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:]) # [:]faz uma cópia da lista dado
    dado.clear()
for p in galera:
    if p[1] >= 21: #se a posição 1 da lista p for maior ou igual a 21 (que é a idade)
        print(f'{p[0]} é maior de idade.') # imprima o nome da pessoa da posição 0
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1