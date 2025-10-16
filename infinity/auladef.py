def cadastrar_produto(nome, preco, categoria='Geral', estoque=0, ativo=True ):
    return {
        'nome': nome,
        'preco': preco,
        'categoria': categoria,
        'estoque': estoque,
        'ativo': ativo,
    }
    
produto1 = cadastrar_produto('produto B', 29.99)