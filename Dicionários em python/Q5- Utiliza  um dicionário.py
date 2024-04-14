#5-Faça um programa, utilizando Dicionários, que:
1° Passo: Peça para o usuário inserir o nome de três funcionários e os mostre na tela.
2° Passo: Peça para o usuário demitir um funcionário e mostre na tela os funcionários restantes.


funcionarios = {}
for i in range(3):
    nome_funcionario = input(f"1° Passo: Insira o nome do funcionário {i+1}: ")
    funcionarios[i+1] = nome_funcionario


print("\nFuncionários:")
for chave, valor in funcionarios.items():
    print(f"{chave}: {valor}")


numero_demitir = int(input("\n2° Passo: Insira o número do funcionário a ser demitido (1, 2 ou 3): "))


if numero_demitir in funcionarios:

    funcionario_demitido = funcionarios.pop(numero_demitir)
    print(f"Funcionário {numero_demitir} ({funcionario_demitido}) foi demitido.")
else:
    print(f"Desculpe, o número {numero_demitir} não corresponde a um funcionário válido.")


print("\nFuncionários restantes:")
for chave, valor in funcionarios.items():
    print(f"{chave}: {valor}")
