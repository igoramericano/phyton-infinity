
def area(l,c):
    a = l * c
    print(f'A área é de {a}m²')
l = float(input('Digite  a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
a = l * c
area(l,c)

print(f'A largura informada foi {l} e o comprimento de {c}, obtendo uma área de {a}m²')