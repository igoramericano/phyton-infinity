lista = []

while True:
    num = int(input("Digite um número: "))
    lista.append(num)
    continuar = input("Quer continuar? (s/n): ").strip().lower()
    if continuar == 's':
        continue
    elif continuar == 'n':
        break
    else:
        print("Resposta inválida. Por favor, responda com 's' ou 'n'.")
    
print("-=" * 30)
print(f'Você digitou {len(lista)} elementos.')
print("-=" * 30)
lista.sort(reverse=True) # Ordena a lista em ordem decrescente
print(f'A lista em ordem decrescente é: {lista}.')
print("-=" * 30)
if 5 in lista:
    print("O valor 5 faz parte da lista!")
else:
    print("O valor 5 não foi encontrado na lista!")
print("-=" * 30)
