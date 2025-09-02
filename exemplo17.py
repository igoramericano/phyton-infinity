# Pede ao usuário para digitar um número
try:
    num = int(input("Digite um número inteiro: "))
    
    # Assume que o número é primo no começo
    eh_primo = True

    # Números menores ou iguais a 1 não são primos
    if num <= 1:
        eh_primo = False
    else:
        # Percorre os números de 2 até o número digitado - 1
        for i in range(2, num):
            # Se o número for divisível por algum deles, não é primo
            if num % i == 0:
                eh_primo = False
                break  # Para o loop assim que encontrar um divisor

    # Exibe o resultado
    if eh_primo:
        print(f"O número {num} é primo.")
    else:
        print(f"O número {num} não é primo.")

except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro.")