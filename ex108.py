import ex107a as moeda

p = float(input('Digite o preço: R$'))
t = int(input('Digite a taxa do reajuste: %'))
print(f'A metade do preço é de {moeda.metade(p)}')
print(f'O dobro do preço é de R${moeda.dobro(p)}')
print(f'{t}% de aumento em R${p} é R${moeda.aumentar(p, t)}')
print(f'{t}% de redução em R${p} é R${moeda.diminuir(p, t)}')


