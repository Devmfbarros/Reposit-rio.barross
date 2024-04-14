#6-Faça um programa, de sua escolha, que utilize Dicionários.

lista_compras = {}

def adicionar_item():
    nome_produto = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade desejada: "))
    preco_unitario = float(input("Digite o preço unitário do produto: R$ "))

    lista_compras[nome_produto] = {'quantidade': quantidade, 'preco_unitario': preco_unitario}

def visualizar_lista():
    print("\nLista de Compras:")
    for produto, info in lista_compras.items():
        print(f"{produto}: {info['quantidade']} unidades, Preço unitário: R$ {info['preco_unitario']:.2f}")

def calcular_custo_total():
    custo_total = sum(info['quantidade'] * info['preco_unitario'] for info in lista_compras.values())
    print(f"\nCusto total das compras: R$ {custo_total:.2f}")


while True:
    print("\nMenu:")
    print("1. Adicionar item à lista")
    print("2. Visualizar lista de compras")
    print("3. Calcular custo total")
    print("4. Sair")

    opcao = input("Escolha uma opção (1-4): ")

    if opcao == '1':
        adicionar_item()
    elif opcao == '2':
        visualizar_lista()
    elif opcao == '3':
        calcular_custo_total()
    elif opcao == '4':
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Escolha uma opção de 1 a 4.")
