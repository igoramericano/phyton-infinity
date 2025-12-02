galera = list()
soma = media = 0
while True:
    pessoa = dict()
    pessoa['nome'] = str(input('Digite o nome: '))
    while True:
        pessoa['sexo'] = str(input('Digite o sexo: [M/F] ').upper()[0])
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Digite apenas M ou F.')
    while True:
        idade = input('Digite a idade: ')
        if idade.isnumeric():
            pessoa['idade'] = int(idade)
            break
        else:
            print('ERRO! Digite um número inteiro para a idade.')
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ').upper()[0])
        if resp in 'SN':
            break
        print('ERRO! Digite apenas S ou N: ')
    if resp == 'N':
        break

print('-' * 30)
print(f'\n Ao todo temos {len(galera)} pessoas cadastradas')

# Lógica da soma
for p in galera:
    soma += p['idade']

# O restante do seu código foi mantido
media = soma / len(galera)
print(f'A média da idade é de {media:5.2f} anos')
print('=' * 30)
print('d) Lista de pessoas do sexo feminino: ')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}')
print('=' * 30)
print('e) Lista de pessoas acima da média: ')
for p in galera:
    if p['idade'] >= media:
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}')
        print()
print('<E N C E R R A D O>')