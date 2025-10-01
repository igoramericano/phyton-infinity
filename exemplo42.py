a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b #junta duas tuplas em ordem, não substitui nem soma, apenas os ordena
print(c)
print(c.count(5)) #conta quantas vezes o número 5 aparece na tupla
print(c.index(4)) #mostra o índice do número 4 na tupla

pessoa = ('Igor', 27, 'M', 75.5)
print (f'O {pessoa[0]} tem {pessoa[1]} anos, é do sexo {pessoa[2]} e pesa {pessoa[3]}kg.')