from ex107a import moeda, dobro, metade, aumentar, diminuir 

p = float(input('Digite o preço: R$'))
t = int(input('Digite a taxa do reajuste: %'))


print(f'A metade do preço é de {moeda(metade(p))}')
print(f'O dobro do preço é de {moeda(dobro(p))}')
print(f'{t}% de aumento em {moeda(p)} é {aumentar(p, t, formato=True)}')
print(f'{t}% de redução em {moeda(p)} é {diminuir(p, t, formato=True)}')
