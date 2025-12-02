# --- INICIALIZAÇÃO DE VARIÁVEIS ---
# O contador: variável que controla o laço de repetição.
# Ele começa em 1 e vai até 10.
contador = 1

# O acumulador para a soma total:
# Ele armazena a soma de todos os números. Começa em zero.
soma_total = 0

# O acumulador para a contagem de números pares:
# Ele conta quantos números pares o laço encontra. Começa em zero.
contador_pares = 0

# --- LAÇO DE REPETIÇÃO WHILE ---
# A condição: o laço continua ENQUANTO o contador for menor ou igual a 10.
while contador <= 10:
    # A cada volta, o valor do contador é adicionado ao acumulador 'soma_total'.
    # Isso acumula a soma de todos os números de 1 a 10.
    soma_total += contador

    # Uma CONDIÇÃO para verificar se o número atual é par.
    # O '%' é o operador de resto da divisão. Se o resto da divisão por 2 for 0, o número é par.
    if contador % 2 == 0:
        # Se a condição for verdadeira (o número é par),
        # adicionamos 1 ao acumulador 'contador_pares'.
        contador_pares += 1
        
    # --- ATUALIZAÇÃO DO CONTADOR ---
    # Adicionamos 1 ao contador a cada volta do laço para evitar um loop infinito.
    # É isso que faz o laço progredir.
    contador += 1

# --- FIM DO LAÇO E IMPRESSÃO DOS RESULTADOS ---
# Quando o contador chega a 11, a condição 'contador <= 10' se torna falsa e o laço para.
# As linhas abaixo são executadas apenas depois que o laço termina.
print(f'A soma de todos os números de 1 a 10 é: {soma_total}')
print(f'O total de números pares encontrados é: {contador_pares}')