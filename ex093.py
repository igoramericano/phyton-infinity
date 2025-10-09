jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: ')) #input nome
print('-' * 30)
tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?: ')) #input qntd partidas
print('-' * 30)
for c in range(0, tot): #loop de 0 ao total de partidas informado acima
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['gols'] = partidas [:]
jogador['total'] =(f'{sum(partidas)} gols')
print('-' * 30)
print(jogador)
print('-' * 30)
print(partidas)
