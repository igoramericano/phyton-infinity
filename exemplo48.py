def saudar_pessoa(nome):
    if nome.lower() == 'todos' or nome.lower() == 'galera':
        print('Olá galera')
    else:
        print(f'Olá, {nome}!')


nome_digitado = input('Digite seu nome: ')
saudar_pessoa(nome_digitado)