temp = []
princ = []

while True:
    temp.append(str(input('Digite um Nome: ')))
    temp.append(float(input('Digite um peso: ')))
    princ.append(temp[:])  # Adiciona uma cópia de temp em princ
    temp.clear()  # Limpa a lista temporária para a próxima iteração
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'Nn':
        break

# LÓGICA CORRIGIDA A PARTIR DAQUI
# Inicializa as variáveis maior e menor com o peso da primeira pessoa
maior = menor = princ[0][1]

# Percorre a lista 'princ' a partir da SEGUNDA pessoa (índice 1)
# para comparar os pesos
for p in princ[1:]:
    # Verifica se o peso da pessoa atual é maior que o maior peso
    if p[1] > maior:
        maior = p[1]
    
    # Verifica se o peso da pessoa atual é menor que o menor peso
    if p[1] < menor:
        menor = p[1]

# O resto da sua lógica de impressão está correta e foi mantida
for p in princ:
    if p[1] == maior:
        print(f'\n Pessoas com o maior peso: {p[0]}')
    if p[1] == menor:
        print(f'Pessoas com o menor peso: {p[0]}')
print('-' * 30)
print(f'Os dados foram: {princ}.')
print('-' * 30)
print(f'Ao todo, você cadastrou {len(princ)} pessoas.')
print('-' * 30)
print(f'O maior peso foi {maior}')
print('-' * 30)
print(f'O menor peso foi {menor}')
print('-' * 30)