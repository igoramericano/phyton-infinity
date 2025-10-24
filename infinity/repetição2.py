def contar_palavras(frase):
    palavras = frase.lower().split()
    palavras_contadas = set()
    contagem = {}

    for palavra in palavras:
        if palavra in palavras_contadas:
            # Palavra já existe na contagem, incrementar contador
            contagem[palavra] += 1
        else:
            # Primeira vez que vemos esta palavra
            palavras_contadas.add(palavra)
            contagem[palavra] = 1
    
    return contagem

# Testando a função
frase1 = str(input('Digite a primeira frase: '))
print(contar_palavras(frase1))

frase2 = str(input('Digite a segunda frase: '))
print(contar_palavras(frase2))

frase3 = str(input('Digite a terceira frase: '))
print(contar_palavras(frase3))  