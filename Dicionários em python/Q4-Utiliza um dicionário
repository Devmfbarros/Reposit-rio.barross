#4-Faça um programa, utilizando Dicionários, que:
1° Passo: Peça para o usuário inserir quatro coisas em uma “Caixa Misteriosa” .
2° Passo: Peça para o usuário inserir um número.
3° Passo: Mostre na tela o que foi inserido na posição do número inserido pelo usuário.

caixa_misteriosa = {}
for i in range(4):
    item = input(f"1° Passo: Insira a {i+1}ª coisa na Caixa Misteriosa: ")
    caixa_misteriosa[i+1] = item


numero_usuario = int(input("\n2° Passo: Insira um número para descobrir o que está na Caixa Misteriosa: "))

if numero_usuario in caixa_misteriosa:
    item_selecionado = caixa_misteriosa[numero_usuario]
    print(f"\nNa posição {numero_usuario} da Caixa Misteriosa, temos: {item_selecionado}")
else:
    print(f"\nDesculpe, o número {numero_usuario} não corresponde a uma posição válida na Caixa Misteriosa.")
