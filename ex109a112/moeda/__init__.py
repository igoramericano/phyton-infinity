def aumentar(p = 0, t1 = 0, formato = False):
    res = p + (p * t1 / 100)
    return res if formato is False else moeda(res)

def diminuir(p = 0, t1 = 0, formato = False):
    res = p - (p * t1 / 100)
    return res if formato is False else moeda(res)

def dobro(p = 0, formato=False):
    res = p * 2
    return res if formato is False else moeda(res)

def metade(p = 0, formato=False):
    res = p / 2
    return res if formato is False else moeda(res)

def moeda(p = 0, moeda_simb = 'R$'):
    return f'{moeda_simb}{p:.2f}'.replace('.', ',')

def resumo(preco=0, t1=10, t2=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preco analisado: \t{moeda(preco)}')
    print(f'Dobro do preco: \t{dobro(preco, True)}')
    print(f'Metade do preco: \t{metade(preco, True)}')
    print(f'{t1}% de aumento: \t{aumentar(preco, t1, True)}')
    print(f'{t2}% de redução: \t{diminuir(preco, t2, True)}')
    print('-' * 30)

def menutop(frase):
    largura = 30 
    print('-' * largura)
    print(frase.center(largura))
    print('-' * largura)
    
def analize(valor):
    largura = 30 
    valor_formatado = moeda(valor) 
    print(f'VALOR ANALIZADO:{valor_formatado}')
    print('-' * largura)

