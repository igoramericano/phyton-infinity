# Onde todos os recados serão armazenados.
# É uma lista que vai guardar os dicionários de cada recado.
lista_de_recados = []

# Usamos um loop while para permitir o cadastro de vários recados.
# O loop continuará até que o usuário digite 'nao'.
while True:
    print("\n--- Cadastro de Novo Recado ---")

    # Coletando as informações com input
    remetente = input("Digite o nome do remetente: ")
    destinatario = input("Digite o nome do destinatário: ")
    idade = input("Digite a idade do destinatário: ")
    mensagem = input("Digite a mensagem: ")

    # Criando um dicionário para o recado
    # As chaves 'remetente', 'destinatario', etc. organizam os dados.
    recado = {
        "remetente": remetente,
        "destinatario": destinatario,
        "idade": idade,
        "mensagem": mensagem
    }

    # Adicionando o dicionário do recado à lista principal
    lista_de_recados.append(recado)
    print("Recado cadastrado com sucesso!")

    # Pergunta se o usuário quer continuar
    continuar = input("Deseja cadastrar outro recado? (sim/nao): ").lower()
    if continuar != 'sim':
        break # Sai do loop se a resposta não for 'sim'

# Depois de sair do loop, exibimos todos os recados cadastrados
print("\n--- Todos os Recados ---")
if not lista_de_recados:
    print("Nenhum recado foi cadastrado.")
else:
    # Usamos um loop 'for' para percorrer a lista e mostrar cada recado
    for i, recado in enumerate(lista_de_recados, 1):
        print(f"\nRecado {i}:")
        print(f"  Remetente: {recado['remetente']}")
        print(f"  Destinatário: {recado['destinatario']} (Idade: {recado['idade']})")
        print(f"  Mensagem: {recado['mensagem']}")

print("--- Fim do Programa ---")