from time import sleep # 1. IMPORTAÇÃO DA BIBLIOTECA SLEEP
from main6b import DADOS_INICIAIS

class Pessoa:
    """Classe base para atributos de uma pessoa."""
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def calcular_idade(self):
        return self.idade

class ContaBancaria:
    """Classe principal para operações bancárias."""
    banco = "Banco Python"

    def __init__(self, titular, saldoInicial=0):
        self.titular = titular
        self.saldo = saldoInicial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado.")
        sleep(1.25) # Timer após o depósito

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")
            sleep(1.25) # Timer após o saque de sucesso
            return True
        else:
            print("Operação cancelada: Saldo insuficiente!")
            sleep(1.25) # Timer após o erro de saldo
            return False

# LÓGICA PRINCIPAL DO BANCO

# Variável para guardar a instância da conta logada
conta_ativa = None

# FUNÇÃO DE BUSCA/LOGIN (mantida do código anterior)
def buscar_conta(num_conta):
    """Busca os dados brutos da conta na lista DADOS_INICIAIS."""
    for dados in DADOS_INICIAIS:
        if dados['numero'] == num_conta:
            return dados
    return None

# FUNÇÃO DE OPERAÇÕES (mantida do código anterior)
def menu_operacoes():
    """Exibe o menu de operações e retorna a escolha do usuário."""
    print("-" * 30)
    print(f"Bem-vindo(a), {conta_ativa.titular}!")
    print(f"Saldo atual: R${conta_ativa.saldo:.2f}")
    print("-" * 30)
    print("1 - DEPOSITAR")
    print("2 - SACAR")
    print("3 - SAIR/LOGOUT")
    print("-" * 30)
    try:
        opc = int(input("Escolha a operação: "))
        return opc
    except ValueError:
        return 0

# --- LOOP PRINCIPAL DO PROGRAMA ---
while True:
    if conta_ativa is None:
        # TELA DE LOGIN
        print("\n--- TELA DE LOGIN ---")
        try:
            num_login = int(input("Digite o número da conta (1001 a 1003) ou 0 para Sair: "))
        except ValueError:
            print("Entrada inválida. Tente novamente.")
            sleep(1.25) # Timer após erro de input
            continue
            
        if num_login == 0:
            print("Obrigado por usar o Banco Python!")
            sleep(1.25)
            break

        # Tenta encontrar a conta nos dados
        dados_encontrados = buscar_conta(num_login)
        
        if dados_encontrados:
            # Se a conta for encontrada, cria a instância
            conta_ativa = ContaBancaria(
                dados_encontrados['titular'],
                dados_encontrados['saldo']
            )
            print(f"Login realizado com sucesso! Olá, {conta_ativa.titular}.")
            sleep(1.25) # Timer após login de sucesso
        else:
            print("Conta não encontrada. Tente novamente.")
            sleep(1.25) # Timer após falha no login
            
    else:
        # TELA DE OPERAÇÕES
        opcao = menu_operacoes()
        
        if opcao == 1:
            try:
                valor = float(input("Digite o valor do depósito: R$"))
                conta_ativa.depositar(valor)
            except ValueError:
                print("Valor inválido. Digite um número.")
                sleep(1.25)
            
        elif opcao == 2:
            try:
                valor = float(input("Digite o valor do saque: R$"))
                # A função sacar() já contém o sleep para sucesso ou erro
                conta_ativa.sacar(valor) 
            except ValueError:
                print("Valor inválido. Digite um número.")
                sleep(1.25)
            
        elif opcao == 3:
            # Sair da conta e voltar para a tela de login
            conta_ativa = None
            print("Sessão encerrada. Volte para fazer login.")
            sleep(1.25)

        else:
            print("Opção inválida. Tente 1, 2 ou 3.")
            sleep(1.25)