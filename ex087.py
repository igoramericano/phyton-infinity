# A variável 'saldo' deve ser global para ser alterada pelas funções
saldo = 1000
print('-' * 30)
print(f'Seu saldo disponivel é de {saldo}')
print('-' * 30)

# A função 'depositar' agora usa a palavra-chave global
def depositar(valor):
    global saldo
    saldo += valor

# A função 'sacar' também usa a palavra-chave global
def sacar(valor):
    global saldo
    saldo -= valor

while True:
    opcao = int(input('Digite a opção: 1- depósito, 2- saque: '))

    if opcao == 1:
        valor_deposito = int(input('Digite o valor para adicionar: '))
        depositar(valor_deposito)
        print(f'Depósito de R${valor_deposito} realizado. Saldo atual: R${saldo}.')

    elif opcao == 2:
        valor_saque = int(input('Digite o valor para sacar: '))
        # A verificação de saldo deve ser feita ANTES do saque
        if valor_saque > saldo:
            print('Saldo insuficiente.')
        elif valor_saque <= saldo:
            # O saque só é realizado se o saldo for suficiente
            sacar(valor_saque)
            print(f'Saque de R${valor_saque} realizado. Saldo atual: R${saldo}.')

    else:
        print('Opção inválida.')

    continuar = input('Quer continuar?: S/N ').strip().lower()[0]
    if continuar in 'Nn':
        print('-' * 30)
        print('Obrigado por utilizar o AMERICANO 24 HORAS')
        print('-' * 30)
        break