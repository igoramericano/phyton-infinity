print('-' * 30)
print('Lojas Americano')
print('-' * 30)
# A lista que vai guardar todos os produtos (dicionários)
produtos = []
total_gasto = 0
produtos_mais_de_mil = 0
produto_mais_barato = 0
nome_produto_barato = ''
while True:
    
    nome_produto = input('Digite o nome do produto ou "sair" para encerrar: ').strip().lower()
    if nome_produto == 'sair':
        break
    else:
        preco_produto = float(input(f'Digite o preço de {nome_produto}: '))

        produtos.append({'nome': nome_produto, 'preco': preco_produto})
        print(f'Produto {nome_produto} adicionado com sucesso!')
for produto in produtos:
    total_gasto += produto['preco']
    if produto['preco'] > 1000:
        produtos_mais_de_mil += 1
    if produto_mais_barato == 0 or produto['preco'] < produto_mais_barato:
        produto_mais_barato = produto['preco']
        nome_produto_barato = produto['nome']
print('-' * 30)
print('Lojas Americano')
print('-' * 30)
print(f'Total gasto na compra: R$ {total_gasto:.2f}')
print(f'Quantidade de produtos que custam mais de R$ 1000.00: {produtos_mais_de_mil}')
print(f'O produto mais barato foi "{nome_produto_barato}" que custa "R$ {produto_mais_barato:.2f}"')   
