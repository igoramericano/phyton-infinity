alunos = {'Nome': 'Igor', 'nota1': 7.0, 'nota2': 7.0,'nota3': 7.0,}

alunos['Nome'] = str(input('Digite seu nome: '))
alunos['nota1'] = float(input('Digite a primeira nota: '))
alunos['nota2'] = float(input('Digite a segunda nota: '))
alunos['nota3'] = float(input('Digite a terceira nota: '))

media = (alunos['nota1'] + alunos['nota2'] + alunos['nota3'] ) / 3

if media >= 7:
    alunos['Situacao'] = 'APROVADO'
elif media >= 5:
    alunos['Situacao'] = 'RECUPERACAO'
else:
    alunos['Situacao'] = 'REPROVADO'

print('-' * 30)
print(f'Nome: {alunos['Nome']}')
print('-' * 30)
print(f'Média {media}')
print('-' * 30)
print(f'Situação: {alunos["Situacao"]}')
print('-' * 30)