from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['RG'] = int(input('Digite o RG: '))

if dados['RG'] !=0:
    print('-' * 30)
    dados['contratação'] = int(input('Ano de contratação: '))
    print('-' * 30)
    dados['salário'] = float(input('Salário: R$'))
    print('-' * 30)
    dados['aposentadoria'] = ((dados['contratação'] + 35) - datetime.now().year)
print('-' * 30)
print(dados)