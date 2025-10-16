import random
import os

# --- 1. BASE DE DADOS E CONFIGURAÇÃO INICIAL ---
contas = [
    {'titular': 'Ana', 'saldo': random.uniform(500, 5000), 'extrato': []},
    {'titular': 'Beto', 'saldo': random.uniform(500, 5000), 'extrato': []},
    {'titular': 'Carlos', 'saldo': random.uniform(500, 5000), 'extrato': []},
    {'titular': 'Daniela', 'saldo': random.uniform(500, 5000), 'extrato': []},
    {'titular': 'Elisa', 'saldo': random.uniform(500, 5000), 'extrato': []}
]

# --- 2. FUNÇÕES DE LÓGICA (O "MOTOR" DO CAIXA) ---

def encontrar_conta(nome_titular):
    """Procura uma conta na lista pelo nome e retorna o dicionário da conta ou None."""
    for conta in contas:
        if conta['titular'].lower() == nome_titular.lower():
            return conta
    print("\nConta não encontrada.")
    return None

def realizar_deposito(conta):
    """Realiza a operação de depósito em uma conta informada."""
    valor = float(input("Digite o valor do depósito: "))
    if valor > 0:
        conta['saldo'] += valor
        conta['extrato'].append(f"Depósito: +R${valor:.2f}")
        print(f"\nDepósito de R${valor:.2f} realizado com sucesso.")
    else:
        print("\nValor inválido para depósito.")

def realizar_saque(conta):
    """Realiza a operação de saque em uma conta informada."""
    valor = float(input("Digite o valor do saque: "))
    if valor <= 0:
        print("\nValor inválido para saque.")
    elif valor > conta['saldo']:
        print("\nSaldo insuficiente.")
    else:
        conta['saldo'] -= valor
        conta['extrato'].append(f"Saque: -R${valor:.2f}")
        print(f"\nSaque de R${valor:.2f} realizado com sucesso.")

def mostrar_extrato(conta):
    """Mostra o extrato de uma conta informada."""
    print(f"\n--- Extrato da conta de: {conta['titular']} ---")
    print(f"Saldo atual: R${conta['saldo']:.2f}")
    print("\n--- Histórico de Transações ---")
    if not conta['extrato']:
        print("Nenhuma transação registrada.")
    else:
        for transacao in conta['extrato']:
            print(transacao)

def realizar_transferencia(conta_origem):
    """Realiza a transferência entre duas contas."""
    nome_destino = input("Digite o nome do titular da conta de destino: ")
    conta_destino = encontrar_conta(nome_destino)
    
    if conta_destino and conta_destino != conta_origem:
        valor = float(input("Digite o valor a ser transferido: "))
        if valor <= 0:
            print("\nValor inválido para transferência.")
        elif valor > conta_origem['saldo']:
            print("\nSaldo insuficiente.")
        else:
            conta_origem['saldo'] -= valor
            conta_destino['saldo'] += valor
            conta_origem['extrato'].append(f"Transferência enviada: -R${valor:.2f} para {conta_destino['titular']}")
            conta_destino['extrato'].append(f"Transferência recebida: +R${valor:.2f} de {conta_origem['titular']}")
            print(f"\nTransferência de R${valor:.2f} realizada com sucesso.")

def listar_contas():
    """Mostra o nome de todos os titulares de contas."""
    print("\n--- Contas Cadastradas no Sistema ---")
    for conta in contas:
        print(f"- {conta['titular']}")

def sair():
    """Encerra o programa."""
    print("\nObrigado por usar nosso sistema. Volte sempre!")
    return False # Retorna False para sinalizar que o loop deve parar

# --- 3. FUNÇÕES DE MENU (O "PAINEL DE CONTROLE") ---
# Funções que pedem o nome do titular antes de chamar a lógica principal.

def menu_deposito():
    conta = encontrar_conta(input("Digite o nome do titular para o depósito: "))
    if conta: realizar_deposito(conta)

def menu_saque():
    conta = encontrar_conta(input("Digite o nome do titular para o saque: "))
    if conta: realizar_saque(conta)

def menu_extrato():
    conta = encontrar_conta(input("Digite o nome do titular para ver o extrato: "))
    if conta: mostrar_extrato(conta)

def menu_transferencia():
    conta = encontrar_conta(input("Digite o nome do titular da sua conta (origem): "))
    if conta: realizar_transferencia(conta)

# --- 4. LOOP PRINCIPAL ---

# Usamos um dicionário para mapear a opção do usuário à função correspondente.
# Isso elimina a necessidade de um 'if/elif/else' gigante.
operacoes = {
    '1': menu_saque,
    '2': menu_transferencia,
    '3': menu_deposito,
    '4': menu_extrato,
    '5': listar_contas,
}

rodando = True
while rodando:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("--- Bem-vindo ao Caixa 24/7 (Versão Simplificada) ---")
    print("\n[1] Saque\n[2] Transferência\n[3] Depósito\n[4] Extrato\n[5] Listar Contas\n[6] Sair")
    
    opcao = input("\nEscolha uma opção: ")

    if opcao == '6':
        rodando = sair()
    else:
        # Pega a função correspondente à opção no dicionário 'operacoes'.
        # Se a opção não existir, 'get' retorna None.
        funcao_a_executar = operacoes.get(opcao)
        if funcao_a_executar:
            funcao_a_executar() # Executa a função encontrada
        else:
            print("\nOpção inválida. Tente novamente.")
    
    if rodando: # Só pausa se o programa não estiver prestes a fechar
        input("\nPressione Enter para continuar...")