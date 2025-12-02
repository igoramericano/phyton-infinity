''' #forma 1
num = int(input('Digite um número '))
n = str(num) #converti num pra string (era inteiro)
print('Analizando o número'.format(num))
print('Milhar: {}'.format(n[0]))
print('Centena: {}'.format(n[1]))
print('Dezena: {}'.format(n[2]))
print('Unidade: {}'.format(n[3]))
'''
''''''#forma 2
num = int(input('Digite um número '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analizando o número'.format(num))
print('Milhar: {}'.format(m))
print('Centena: {}'.format(c))
print('Dezena: {}'.format(d))
print('Unidade: {}'.format(u))