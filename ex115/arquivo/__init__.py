from ex115.interface import cabeçalho

def arquivoExiste(nome):
    try:
        # 'with' garante que o arquivo seja fechado
        with open(nome, 'rt'):
            return True
    except FileNotFoundError:
        return False

def criarArquivo(nome):
    try:
        with open(nome, 'wt+'):
            pass # Cria e fecha
    except Exception:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArquivo(nome):
    try:
        # 'with' evita erro de 'a.close()' se o open falhar
        with open(nome, 'rt') as a: 
            cabeçalho('Pessoas cadastradas!')
            for linha in a:
                linha = linha.strip() # Remove '\n'
                if linha:
                    dado = linha.split(';')
                    # Assumindo formato 'Nome;Idade'
                    nome_cadastrado = dado[0].strip()
                    idade_cadastrada = dado[1].strip() if len(dado) > 1 else '?'
                    print(f'Nome: {nome_cadastrado:<20} Idade: {idade_cadastrada}')
    except FileNotFoundError:
        print(f'Erro: Arquivo "{nome}" não encontrado!')
    except Exception:
        print('Erro ao ler o arquivo!')


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        # 'at' para anexar (append text)
        with open(arq, 'at') as a: 
            a.write(f'{nome};{idade}\n') # Escreve no formato Nome;Idade\n
        print(f'Novo registro de {nome} adicionado')
    except Exception:
        print('ERRO ao exibir dados/salvar!')