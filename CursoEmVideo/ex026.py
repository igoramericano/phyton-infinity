frase = str(input('Digite uma frase: ')).lower().strip()
print('A letra a aparece {} vezes na frase.' .format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('a')+1))