nome = str(input('Digite seu nome completo: ')) .strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
# print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
#a linha de cima, ou seja, "tamanho do nome MENOS a contagem de espaços", faz contar só as letras
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

