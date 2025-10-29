def leiadinheiro(mensagem='Digite um valor: R$'):
    valido = False
    while not valido:
        entrada_str = input(mensagem).strip()
        entrada_formatada = entrada_str.replace(',', '.')
    
        if entrada_formatada.replace('.', '', 1).isdigit() and entrada_formatada.count('.') <= 1:
            valor = float(entrada_formatada)
            
            print(f'Valor lido: R${valor:.2f}'.replace('.', ','))
            print('-'*30)
            valido = True
            return valor
        else:
            print(f'\033[0;31mERRO! "{entrada_str}" é um preço inválido!\033[m')