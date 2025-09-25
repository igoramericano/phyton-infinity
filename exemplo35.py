# Exemplo 35: Laço for com range e passo personalizado
inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))
passo = int(input("Digite o passo: "))


if passo == 0:
    print("Erro: O passo não pode ser zero.")
else:
    for numero in range(inicio, fim, passo):
        print(numero)
    print("FIM")