# --- 1. CLASSES DE POO ---

class bankacc:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor
        print(f"\nDepósito de R${valor:.2f} realizado na conta de {self.titular}.")

    def sacar(self, valor):
        if valor <= self.saldo: 
            self.saldo -= valor
            print(f"\nSaque de R${valor:.2f} realizado com sucesso na conta de {self.titular}.")
        else:
            print("\n❌ Saldo insuficiente! Operação cancelada.")
            
    def transferir(self, conta_destino, valor):
        # A lógica de saque (verificação de saldo) e depósito é combinada aqui
        if valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor 
            print(f"\n✅ Transferência de R${valor:.2f} para {conta_destino.titular} realizada com sucesso.")
        else:
            print("\n❌ Saldo insuficiente para realizar a transferência.")
            
    def extrato(self):
        print(f"\n--- Extrato da Conta de {self.titular} ---")
        print(f"Saldo Atual: R${self.saldo:.2f}")

class ContaPoupanca(bankacc):
    def __init__(self, titular, saldo=0):
        # Chama o construtor da classe base (bankacc)
        bankacc.__init__(self, titular, saldo)
    
    def render_juros(self):
        self.saldo *= 1.01
        print(f"\nJuros de 1% aplicados na conta de {self.titular}. Novo saldo: R${self.saldo:.2f}")


# --- 2. CONFIGURAÇÃO E ARMAZENAMENTO DE CONTAS ---

# Contas Poupança de Igor e Amanda, armazenadas em um dicionário para fácil busca
CONTAS = {
    "IGOR": ContaPoupanca("Igor", 500.00),
    "AMANDA": ContaPoupanca("Amanda", 200.00)
}


# --- 3. FUNÇÃO DE SELEÇÃO/LOGIN ---

def selecionar_conta():
    while True:
        print("\n" + "="*40)
        print("🏦 Seleção de Conta - Banco POO")
        print("Titulares: Igor, Amanda")
        print("="*40)
        
        nome_titular = input("Digite o nome do titular (ou 'sair'): ").upper() # Padroniza para maiúsculas
        
        if nome_titular == 'SAIR':
            print("Saindo do sistema. Até logo!")
            return None # Retorna None para encerrar o programa
            
        if nome_titular in CONTAS:
            return CONTAS[nome_titular] # Retorna o objeto ContaPoupanca
        else:
            print("❌ Conta não encontrada. Tente novamente.")

# --- 4. FUNÇÃO DE OPERAÇÕES (MENU SECUNDÁRIO) ---

def operacoes_conta(conta_atual):
    titular = conta_atual.titular
    
    while True:
        print("\n" + "#"*40)
        print(f"Conta Selecionada: {titular} | Saldo: R${conta_atual.saldo:.2f}")
        print("#"*40)
        
        print("1. Depositar")
        print("2. Sacar")
        print("3. Transferir")
        print("4. Render Juros")
        print("5. Extrato")
        print("6. Trocar de Conta / Sair")
        
        escolha = input("Escolha uma opção (1-6): ")

        try:
            if escolha in ('1', '2', '3'):
                valor = float(input("Digite o valor da operação: R$"))
                if valor <= 0:
                    print("O valor deve ser positivo.")
                    continue
            
            if escolha == '1':
                conta_atual.depositar(valor)

            elif escolha == '2':
                conta_atual.sacar(valor)

            elif escolha == '3':
                # Transferência Dinâmica
                receptor_nome = input("Digite o NOME do titular que receberá a transferência: ").upper()
                
                if receptor_nome in CONTAS and receptor_nome != titular.upper():
                    conta_destino = CONTAS[receptor_nome]
                    conta_atual.transferir(conta_destino, valor)
                elif receptor_nome == titular.upper():
                    print("❌ Não é possível transferir para a mesma conta.")
                else:
                    print(f"❌ Conta de destino '{receptor_nome}' não encontrada.")
            
            elif escolha == '4':
                # Render Juros só funciona em ContaPoupanca
                if isinstance(conta_atual, ContaPoupanca):
                    conta_atual.render_juros()
                else:
                    print("Essa conta não é uma Conta Poupança e não possui rendimento de juros.")

            elif escolha == '5':
                conta_atual.extrato()
            
            elif escolha == '6':
                return # Volta para o menu principal de seleção

            else:
                print("\nOpção inválida. Tente novamente.")
        
        except ValueError:
            print("\nErro: Por favor, digite um número válido.")


# --- 5. LOOP PRINCIPAL DE EXECUÇÃO ---

def main():
    while True:
        conta_selecionada = selecionar_conta()
        
        if conta_selecionada is None:
            break # Sai do loop se selecionar_conta retornar None
        
        # Inicia o menu de operações para a conta selecionada
        operacoes_conta(conta_selecionada) 

if __name__ == "__main__":
    main()