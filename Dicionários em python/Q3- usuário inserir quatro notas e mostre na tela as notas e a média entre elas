#3-Faça um programa, utilizando Dicionários, que peça para o usuário inserir quatro notas e mostre na tela as notas e a média entre elas

notas = {}


for i in range(4):
    nota = float(input(f"Insira a nota {i+1}: "))
    notas[f"Nota {i+1}"] = nota

media = sum(notas.values()) / len(notas)


print("\nNotas inseridas:")
for chave, valor in notas.items():
    print(f"{chave}: {valor}")

print(f"Média das notas: {media:.2f}")
