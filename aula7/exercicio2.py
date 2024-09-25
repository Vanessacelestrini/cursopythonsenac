"Elabore um script que solicite o nome de um aluno e duas notas."
"Em seguida calcule e imprima a media e mostre se o aluno foi aprovado ou reprovado, Para estar aprovado a media tem de ser acima de 6,5"
"Faca isso para 3 alunos"

medias = []

num_alunos = int(input("Digite o número de alunos: "))

for i in range(num_alunos):
    nomeAlunos = input(f"Digite o nome do aluno {i + 1}: ")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    
    # Calculando a média
    media = (nota1 + nota2) / 2
    medias.append(media)  

    if media >= 6.5:
        print(f"{nomeAlunos}: Média: {media:.2f} - Foi Aprovado")
    else:
        print(f"{nomeAlunos}: Média: {media:.2f} - Foi Reprovado")

# média geral das médias
media_geral = sum(medias) / num_alunos
print(f"\nMédia Geral da Turma: {media_geral:.2f}")
