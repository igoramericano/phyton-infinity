# Passo 1: Criar o dicionário vazio para armazenar os alunos
# O nome do aluno será a CHAVE e a lista de notas será o VALOR
alunos = {}


num_alunos = 0
# Passo 2: Usar um loop WHILE para cadastrar os alunos
# A variável 'num_alunos' vai controlar quantos alunos serão cadastrados

while num_alunos < 4:
    # Coletar o nome do aluno
    nome = input("Digite o nome do aluno: ")
    
    # Coletar as 3 notas. Usamos input() para pegar o valor e float() para
    # converter para um número com casas decimais
    nota1 = float(input(f"Digite a primeira nota de {nome}: "))
    nota2 = float(input(f"Digite a segunda nota de {nome}: "))
    nota3 = float(input(f"Digite a terceira nota de {nome}: "))
    
    # Armazenar as notas em uma lista
    notas = [nota1, nota2, nota3]
    

    alunos[nome] = notas
    
    
    num_alunos += 1
    
    print("-" * 20)


print("\n--- Resultado Final ---")

# Iterar sobre o dicionário 'alunos'
for nome, notas in alunos.items():
    
    # Calcular a média
    media = sum(notas) / len(notas)
    
    # Verificar se o aluno foi aprovado ou reprovado
    if media >= 7:
        situacao = "APROVADO"
    else:
        situacao = "REPROVADO"
        
    # Exibir o resultado formatado
    # f-string é um jeito simples de inserir variáveis em textos
    print(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}")

print("-----------------------")