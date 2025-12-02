def escreva(palavra):
    print('-' * len(palavra))
    print(f'  {palavra}')
    print('-' * len(palavra))
    
palavra = str(input('Digite a palavra para inserir na paradinha: '))

escreva(palavra)