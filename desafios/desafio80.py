lista = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    
    # A variável 'pos' vai controlar a posição na lista
    pos = 0
    # O loop vai encontrar a posição para o número
    while pos < len(lista):
        # Se o novo número for menor ou igual ao da posição atual,
        # ele encontrou a posição para ser inserido
        if n <= lista[pos]:
            lista.insert(pos, n)
            break
        # Se não, continua procurando a próxima posição
        pos += 1
    # Se o loop terminar sem encontrar uma posição (o número é maior que todos),
    # ele será adicionado no final da lista
    else:
        lista.append(n)

print('-=' * 30)
print(f'Os valores digitados em ordem foram {lista}')