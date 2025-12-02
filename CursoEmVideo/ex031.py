print('-=-'*20)
print('INICIO')
print('-=-'*20)
distancia = int(input('Qual a distância de sua viagem em KM?: '))
if distancia <= 200:
    valor = distancia * 0.50
else:
    valor = distancia * 0.45
print('A sua viagem de {}Km custou R${:.2f}'.format(distancia,valor))
print('-=-'*20)
print('FIM')
print('-=-'*20)