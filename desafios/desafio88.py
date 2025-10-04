import random
import time 
lista = [] # Lista temporária para cada jogo
jogos = [] # Lista principal para guardar todos os jogos

print('-' * 30)
print('JOGUE NA MEGA SENA')
print('-' * 30)
quant = int(input('Quantos jogos você quer que eu sorteie? '))
print('-' * 3, f'SORTEANDO {quant} JOGOS', ' -' * 3)
time.sleep(1)

# Usamos um for loop para repetir a lógica o número de vezes que o usuário pediu
for i in range(0, quant):
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break  
    lista.sort()
    jogos.append(lista[:]) # Adiciona uma cópia da lista em jogos
    lista.clear() # Limpa a lista para o próximo jogo
# Exibe os jogos no final, usando a lista 'jogos'
for i, l in enumerate(jogos):
    time.sleep(1) # Pausa a execução por 1 segundo
    print(f'Jogo {i+1}: {l}')

print('-' * 3, f' BOA SORTE! ', ' -' * 3)