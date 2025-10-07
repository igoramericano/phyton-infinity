alunos = []
while True:
    print('=' * 40)
    print(' MENU DE CADASTRO '.center(40, '='))
    print('=' * 40)
    print('1- Cadastrar aluno')
    print('2- Excluir aluno')
    print('3- Consultar alunos')
    print('4- Atualizar notas')
    print('5- Relatório de aprovação')
    print('0- Sair do programa') # Adicionado opção de sair
    print('=' * 40)
    # Adicionado 'try-except' para evitar erro caso o usuário digite texto
    try:
        n = int(input('Digite a opção desejada: '))
    except ValueError:
        print('Opção inválida. Digite um número.')
        continue # Retorna ao início do loop
    
    if n == 1:
        print('--- Cadastro de Aluno ---')
        nome_aluno = input('Digite o nome do aluno: ')
        aluno_completo = {'nome': nome_aluno, 'notas': []}
        alunos.append(aluno_completo)
        print(f'Aluno {nome_aluno} cadastrado com sucesso!')
        
    elif n == 2:
        print('--- Exclusão de Aluno ---')
        nome_excluir = input('Digite o nome do aluno a ser excluído: ')
        encontrado = False
        
        # Percorre a lista para encontrar e remover o aluno
        for aluno in alunos:
            if aluno['nome'] == nome_excluir:
                alunos.remove(aluno)
                print(f'Aluno {nome_excluir} removido com sucesso.')
                encontrado = True
                break
        if not encontrado:
            print('Aluno não encontrado.')
    
    elif n == 3:
        print('--- Lista de Alunos ---')
        # Verifica se a lista não está vazia antes de imprimir
        if alunos:
            # Imprime cada aluno em uma linha separada para melhor visualização
            for aluno in alunos:
                print(aluno)
        else:
            print('Nenhum aluno cadastrado.')

    elif n == 4:
        print('--- Atualizar Notas ---')
        nome_busca = input('Digite o nome do aluno para adicionar a nota: ')
        aluno_encontrado = None
        
        # Encontra o aluno na lista
        for aluno in alunos:
            if aluno['nome'] == nome_busca:
                aluno_encontrado = aluno 
                break 
        
        if aluno_encontrado:
            # Adiciona uma nova nota e a converte para float
            try:
                nota_nova = float(input(f'Digite a nota para {nome_busca}: '))
                aluno_encontrado['notas'].append(nota_nova)
                print(f'Nota {nota_nova} adicionada para o aluno {nome_busca}.')
            except ValueError:
                print('Entrada inválida. Digite um número para a nota.')
        else:
            print('Aluno não encontrado.')
            
    elif n == 5:
        print('--- Relatório de Aprovação ---')
        
        for aluno in alunos:
            
            if aluno['notas']:
                
                media = sum(aluno['notas']) / len(aluno['notas'])
                if media >= 7.0:
                    situacao = 'APROVADO'
                else:
                    situacao = 'REPROVADO'
                print(f'Aluno: {aluno["nome"]}, Média: {media:.2f}, Situação: {situacao}')
            else:
                print(f'Aluno: {aluno["nome"]}, Situação: Sem notas cadastradas.')
    elif n == 0:
        print('Encerrando o programa. Até a próxima!')
        break 
    else:
        print('Opção inválida. Tente novamente.')