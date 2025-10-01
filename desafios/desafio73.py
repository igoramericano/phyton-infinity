# A tupla 'times' foi atualizada com a ordem da tabela da imagem
times = ('Flamengo', 'Cruzeiro', 'Palmeiras', 'Mirassol', 'Botafogo',
         'Bahia', 'São Paulo', 'Fluminense', 'Bragantino', 'Grêmio',
         'Ceará SC', 'Vasco da Gama', 'Atlético-MG', 'Corinthians', 'Internacional',
         'Santos', 'Juventude', 'EC Vitória', 'Fortaleza', 'Sport Recife')

print('-=' * 20)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 20)
print(f'Os 6 primeiros são: {times[0:6]}')
print('-=' * 20)
print(f'Os 4 últimos são: {times[-4:]}')
print('-=' * 20)
# A busca foi corrigida para um time presente na nova lista: 'Vasco da Gama'
print(f'O EC Vitória está na {times.index('EC Vitória') + 1}ª posição') 
#+1 pq a 1a posição é 0
print('-=' * 20)