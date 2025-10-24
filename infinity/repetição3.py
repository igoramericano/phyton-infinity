alunos = {}
relatório_final = []
num_alunos = 0
while num_alunos < 4:
    nome = input("Digite o nome do aluno: ")
    nota1 = float(input(f"Digite a primeira nota de {nome}: "))
    nota2 = float(input(f"Digite a segunda nota de {nome}: "))
    nota3 = float(input(f"Digite a terceira nota de {nome}: "))
    
    notas = [nota1, nota2, nota3]
    alunos[nome] = notas
    num_alunos += 1
    
    print("-" * 20)


print("\n--- Resultado Final ---")



for nome, notas in alunos.items():
    media = sum(notas) / len(notas)
    if media >= 7:
        situacao = "APROVADO"
    elif media < 7 and media >= 5:
        situacao = "RECUPERAÇÃO"
    else:
        situacao = "REPROVADO"
    print(f"Aluno: {nome} | Média: {media:.2f} | Situação: {situacao}")
    tupla_aluno = (nome, media, situacao)
    relatório_final.append(tupla_aluno)

print("-----------------------")
print(tupla_aluno)
print("-----------------------")