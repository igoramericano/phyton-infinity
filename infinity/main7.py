class Filme:
    def __init__(self, titulo, ano, diretor, genero, duracao):
        self.titulo = titulo
        self.ano = ano
        self.diretor = diretor
        self.genero = genero
        self.duracao = duracao
        self.avaliacoes = []
        self.vizualizacoes = 0
        self.avaliacao_media = 0.0
    
    def reproduzir(self):
        self.vizualizacoes += 1
        print(f"Reproduzindo... Visualizações: {self.vizualizacoes}")
        
    def avaliar(self, nota):
        if 0 <= nota <= 5: 
            self.avaliacoes.append(nota)
            self.avaliacao_media = sum(self.avaliacoes) / len(self.avaliacoes)
            print('Nota registrada!')
        else:
            print('Nota inválida, digite entre 0 e 5.')
            
    def duracao_formatada(self):
        horas = self.duracao // 60
        minutos_restantes = self.duracao % 60
        return f'{horas}h{minutos_restantes}min'

catalogo = []     
n = 0

while n != 4:
    print('-'*30)
    
    # Lê como string primeiro
    opcao_digitada = input('1- Listar, 2- Cadastrar, 3- Excluir, 4- Sair: ')

    # Validação manual: se for número, converte. Se não, força um número inválido (0)
    if opcao_digitada.isnumeric():
        n = int(opcao_digitada)
    else:
        n = 0 

    if n == 1:
        print(">>> LISTAR FILMES <<<")
        if len(catalogo) == 0:
            print("Nenhum filme cadastrado.")
        else:
            for i, filme in enumerate(catalogo):
                print(f"{i} - {filme.titulo} ({filme.ano}) | {filme.duracao_formatada()} | Nota: {filme.avaliacao_media:.1f}")
        
    elif n == 2:
        print(">>> CADASTRAR FILME <<<")
        titulo = input('Digite o titulo do filme: ')
        diretor = input('Digite o diretor do filme: ')
        genero = input('Digite o gênero do filme: ')
        
        # Validação do Ano
        ano_str = input('Digite o ano de lançamento: ')
        if ano_str.isnumeric():
            ano = int(ano_str)
        else:
            print("Ano inválido (definido como 0).")
            ano = 0
            
        # Validação da Duração
        duracao_str = input('Digite a duração em min: ')
        if duracao_str.isnumeric():
            duracao = int(duracao_str)
        else:
            print("Duração inválida (definido como 0).")
            duracao = 0
        
        # Só cadastra se os dados numéricos forem válidos (opcional, mas recomendado)
        if ano > 0 and duracao > 0:
            novo_filme = Filme(titulo, ano, diretor, genero, duracao)
            catalogo.append(novo_filme)
            print("Filme cadastrado com sucesso!")
        else:
            print("Falha ao cadastrar: Ano ou duração inválidos.")
        
    elif n == 3:
        print(">>> EXCLUIR FILME <<<")
        if len(catalogo) == 0:
            print("Lista vazia.")
        else:
            nome_excluir = input("Digite o nome do filme para excluir: ")
            filme_remover = None
            
            # Procura o objeto na lista
            for filme in catalogo:
                if filme.titulo.lower() == nome_excluir.lower():
                    filme_remover = filme
                    break
            
            # Se achou, remove
            if filme_remover:
                catalogo.remove(filme_remover)
                print(f"Filme '{filme_remover.titulo}' removido!")
            else:
                print("Filme não encontrado.")
        
    elif n == 4:
        print('Saindo do sistema... Até logo!')
        break 
        
    else:
        print('Opção inválida! Tente de 1 a 4.')