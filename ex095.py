jogador = dict()
time = list()
partidas = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: '))
    print('-' * 30)
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?: '))
    
    # A lista 'partidas' deve ser limpa ANTES de começar o loop de gols
    partidas.clear() 
    print('-' * 30)
    
    for c in range(0, tot):
        partidas.append(int(input(f'Quantos gols na partida {c+1}? ')))
        
    # A atribuição para o dicionário deve ser feita APÓS o loop de gols
    jogador['gols'] = partidas[:]
    # Armazena o total de gols como um número, não uma string
    jogador['total'] = sum(partidas)
    
    # Adiciona o dicionário do jogador à lista 'time'
    time.append(jogador.copy())
    
    while True:
        resp = str(input('Quer continuar? [S/N]').upper()[0])
        if resp in 'SN':
            break
        print('E R R O! Responda apenas "S" ou "N": ')
    if resp == 'N':
        break

print('-' * 40)
print('Cod', end=' ')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)

# Percorre a lista 'time' para exibir a tabela completa de todos os jogadores
for k, v in enumerate(time):
    print(f'{k:>3}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

print('-' * 40)

# Percorre a lista 'time' para exibir os detalhes de cada jogador
for i, jogador_dict in enumerate(time):
    print(f'O jogador {jogador_dict["nome"]} jogou {len(jogador_dict["gols"])} partidas.')
    for index, gols in enumerate(jogador_dict['gols']):
        print(f'   --> Na partida {index+1}, fez {gols} gols.')
    print(f'Foi um total de {jogador_dict["total"]} gols.')
    print('-' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'E R R O! Não existe jogador com código {busca}')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {time[busca]['nome']}')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i+1} fez {g} gols')
print('-' * 40)
print('E N C E R R A D O! Volte sempre!!')