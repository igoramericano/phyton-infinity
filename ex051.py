def main():
    """
    Função principal que pede um número e verifica se ele é divisível por 2.
    """
    while True:
        try:
            # Pede ao usuário para digitar um número
            num_str = input("Digite um número inteiro (ou 'sair' para encerrar): ")

            if num_str.lower() == 'sair':
                print("Programa encerrado.")
                break

            num = int(num_str)

            # Verifica se o resto da divisão por 2 é 0
            if num % 2 == 0:
                print(f"O número {num} é divisível por 2 com resto 0.")
            else:
                print(f"O número {num} não é divisível por 2 com resto 0.")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro válido.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    main()# exemplo16.py