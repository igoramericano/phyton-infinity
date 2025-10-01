pessoas = [] #coloca essa merda aqui fora do while, senão ele zera a lista toda hora
homens = mulheres = adultos = 0
while True:
    cadastro = str(input('Deseja cadastrar uma pessoa? [S/N] ')).strip().upper()[0]
    if cadastro == 'S':
        nome = str(input('Nome: ')).strip().lower().title()
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        idade = int(input('Idade: '))
        pessoa = {'Nome': nome, 'Sexo': sexo, 'Idade': idade}
        #quando criar um dicionário e usar input, usa o formato acima para declarar as variáveis
        pessoas.append(pessoa)
    elif cadastro == 'N':
        break  

for pessoa in pessoas:
    if pessoa ['Idade'] > 18:
        adultos += 1
    if pessoa ['Sexo'] == 'M'.upper():
        homens += 1
    elif pessoa ['Sexo'] == 'F'.upper() and pessoa ['Idade'] < 20:
        mulheres += 1
    
print(f'Foram cadastradas {len(pessoas)} pessoas com mais de 18 anos.')
print(f'Temos {homens} homens cadastrados.')    
print(f'Temos {mulheres} mulheres com menos de 20 anos.')
        
        