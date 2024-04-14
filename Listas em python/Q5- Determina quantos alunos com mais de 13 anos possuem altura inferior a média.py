#5 - Foram anotadas as idades e alturas de 10 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.


idades = []
alturas = []

for i in range(10):
    idade = int(input(f"Digite a idade do aluno {i + 1}: "))
    altura = float(input(f"Digite a altura (em metros) do aluno {i + 1}: "))

    idades.append(idade)
    alturas.append(altura)


media_altura = sum(alturas) / len(alturas)

alunos_contados = sum(1 for idade, altura in zip(idades, alturas) if idade > 13 and altura < media_altura)


print(f"\nMédia de altura dos alunos: {media_altura} metros")
print(f"Quantidade de alunos com mais de 13 anos e altura inferior à média: {alunos_contados}")
