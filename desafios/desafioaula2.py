# Lista principal que vai guardar os dicionários de carros
carros = []

while True:
    print('=' * 40)
    print(' SISTEMA DE LEITURA DE PLACAS '.center(40, '='))
    print('=' * 40)
    print('1- Cadastrar veículo')
    print('2- Excluir veículo')
    print('3- Consultar veículos')
    print('4- Registrar entrada/saída')
    print('5- Relatório de status')
    print('0- Sair do programa')
    print('=' * 40)
    
    try:
        n = int(input('Digite a opção desejada: '))
    except ValueError:
        print('Opção inválida. Digite um número.')
        continue
    
    if n == 1:
        print('--- Cadastro de Veículo ---')
        placa = input('Digite a placa do veículo (Ex: ABC-1234): ').upper()
        # Dicionário do veículo com uma lista para registrar entradas/saídas
        veiculo_completo = {'placa': placa, 'status_historico': []}
        carros.append(veiculo_completo)
        print(f'Veículo de placa {placa} cadastrado com sucesso!')
        
    elif n == 2:
        print('--- Exclusão de Veículo ---')
        placa_excluir = input('Digite a placa do veículo a ser excluído: ').upper()
        encontrado = False
        
        for veiculo in carros:
            if veiculo['placa'] == placa_excluir:
                carros.remove(veiculo)
                print(f'Veículo de placa {placa_excluir} removido com sucesso.')
                encontrado = True
                break
        if not encontrado:
            print('Veículo não encontrado.')
    
    elif n == 3:
        print('--- Lista de Veículos ---')
        if carros:
            for veiculo in carros:
                print(veiculo)
        else:
            print('Nenhum veículo cadastrado.')

    elif n == 4:
        print('--- Registrar Entrada/Saída ---')
        placa_busca = input('Digite a placa do veículo: ').upper()
        veiculo_encontrado = None
        
        for veiculo in carros:
            if veiculo['placa'] == placa_busca:
                veiculo_encontrado = veiculo 
                break 
        
        if veiculo_encontrado:
            status = input('Digite o status ("Entrada" ou "Saida"): ').capitalize()
            # Adiciona o novo status à lista de histórico do veículo
            veiculo_encontrado['status_historico'].append(status)
            print(f'Status "{status}" registrado para o veículo de placa {placa_busca}.')
        else:
            print('Veículo não encontrado. Cadastre-o primeiro.')
            
    elif n == 5:
        print('--- Relatório de Status ---')
        veiculos_dentro = 0
        
        for veiculo in carros:
            if veiculo['status_historico']:
                ultimo_status = veiculo['status_historico'][-1]
                if ultimo_status == 'Entrada':
                    situacao = 'DENTRO'
                    veiculos_dentro += 1
                else:
                    situacao = 'FORA'
                
                print(f'Placa: {veiculo["placa"]}, Status: {situacao}')
            else:
                print(f'Placa: {veiculo["placa"]}, Status: Sem histórico registrado.')
        
        print(f'\nTotal de veículos DENTRO do estacionamento: {veiculos_dentro}')
    
    elif n == 0:
        print('Encerrando o programa. Até a próxima!')
        break
    
    else:
        print('Opção inválida. Tente novamente.')