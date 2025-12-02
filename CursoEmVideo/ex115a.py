from ex115.interface import * 
from ex115.arquivo import * 
from time import sleep

arq = 'NOMESex115.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Pessoas cadastradas', 'Cadastrar pessoas', 'SAIR do sistema'])
    if resposta == 1:
        lerArquivo(arq) 
    elif resposta == 2:
        sleep(1)
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        lerArquivo(arq)     
    elif resposta == 3:
        cabeçalho('Saindo do sistema, até logo!')
        break
    else:
        print('\033[31mOPÇÃO INVÁLIDA!! Digite de 1 a 3!\033[m')
    sleep(1)