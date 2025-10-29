from ex107a import moeda, dobro, metade, aumentar, diminuir 

p = float(input('Digite o preço: R$'))
t = int(input('Digite a taxa do reajuste: %'))


print(f'A metade do preço é de {moeda(metade(p))}')
print(f'O dobro do preço é de {moeda(dobro(p))}')
print(f'{t}% de aumento em {p} é {aumentar(p, t, formato=True)}')
print(f'{t}% de redução em {p} é {diminuir(p, t, formato=True)}')

# para puxar uma função importada, se usa {função(nomefunção(a))}