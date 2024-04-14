#2-Faça um programa, utilizando Dicionários, que peça para o usuário inserir o nome de três produtos de mercado e seus respectivos preços e os mostre na tela.

produtos = {}


for i in range(3):
    nome_produto = input(f"Insira o nome do produto {i+1}: ")
    preco_produto = float(input(f"Insira o preço do produto {i+1}: R$ "))
    produtos[nome_produto] = preco_produto

print("\nProdutos e Preços:")
for produto, preco in produtos.items():
    print(f"{produto}: R$ {preco:.2f}")
