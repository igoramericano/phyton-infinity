from ex107a import *

p = float(input('Digite o preço: R$'))
t = int(input('Digite a taxa do reajuste: %'))
print(f'A metade do preço é de {metade(p)}')
print(f'O dobro do preço é de {dobro(p)}')
print(f'{t}% de aumento em R${p} é R${aumentar(p, t)}')
print(f'{t}% de redução em R${p} é R${diminuir(p, t)}')


