nome = str(input('Qual é o seu nome? '))

if nome.lower() == 'igor':
    print('Que nome lindo você tem!')
    
elif nome.lower() == 'ana' or nome.lower() == 'maria' or nome.lower() == 'joão':
    print('Seu nome é bem popular no Brasil!')
    
elif nome.lower() in 'pedro paulo carlos gustavo gabriel ana maria joão amanda':
    print('Seu nome é bem comum no Brasil!')   
    
else:
    print('Seu nome é tão normal!')
    