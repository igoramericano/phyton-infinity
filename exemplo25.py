# Definindo as variáveis para o nosso exemplo
nota_do_aluno = 7
idade_da_pessoa = 18

print("--- Exemplo de 'if' ---")
# Aqui, o código verifica se a nota é suficiente para uma menção honrosa.
# Se a condição for verdadeira, a mensagem será exibida. Se for falsa, nada acontece.
if nota_do_aluno >= 9:
    print("Parabéns, você recebeu uma menção honrosa!")

print("\n--- Exemplo de 'if else' ---")
# Este bloco de código decide se o aluno foi aprovado ou reprovado.
# Se a nota for 7 ou mais, o aluno é aprovado. Caso contrário, ele é reprovado.
if nota_do_aluno >= 7:
    print("Aluno aprovado!")
else:
    print("Aluno reprovado.")

print("\n--- Exemplo de 'if elif else' ---")
# Este bloco decide a categoria de uma pessoa com base na idade.
# A primeira condição que for verdadeira é executada e o resto é ignorado.
if idade_da_pessoa < 12:
    print("Criança.")
elif idade_da_pessoa < 18:
    print("Adolescente.")
elif idade_da_pessoa < 60:
    print("Adulto.")
else:
    print("Idoso.")