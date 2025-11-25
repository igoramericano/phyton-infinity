class ContadorDePalavras:
    
    def contar(self, frase):
        """
        Recebe uma string (frase) e retorna o número total de palavras nela.
        A contagem é feita quebrando a frase em uma lista de palavras.
        """
        # Quebra a frase em palavras e usa len() para contar os itens
        lista = frase.split()
        return len(lista)

# Exemplo de uso:
contador = ContadorDePalavras()
frase = input("Digite uma frase para calcular o numero de palavras: ")
total_palavras = contador.contar(frase)
print(f"A frase tem {total_palavras} palavras.")