from ex107a import moeda, dobro, metade, aumentar, diminuir 

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

p = float(input('Digite o preço: R$'))
t = int(input('Insira a % de correção: %'))
menutop("MENU PRINCIPAL")
print(f'A metade de {moeda(p)} é {metade(p, True)}')
print(f'O dobro de {moeda(p)} é {dobro(p, True)}')
print(f'Aumentando {t}%, temos {aumentar(p, t, True)}')
print(f'Reduzindo {t}%, temos {diminuir(p, t, True)}')
analize(p)