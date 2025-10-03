vogais = ('a', 'e', 'i', 'o', 'u', 'á', 'à', 'ã', 'â', 'é', 'è', 'ê', 'í', 'ó', 'ò', 'ô', 'õ', 'ú', 'ü') #assim ele engloba mais variações de vogais
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

for palavra in palavras:
    print(f'\n Na palavra {palavra.lower()} temos |', end='')
    for letra in palavra.lower():
        if letra in vogais:
            print(letra, end=' ')