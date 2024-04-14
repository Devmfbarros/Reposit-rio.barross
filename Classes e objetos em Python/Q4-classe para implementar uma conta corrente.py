#4.Crie uma classe para implementar uma conta corrente. A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo.
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios.
class ContaCorrente:
    def __init__(self, numero_conta, nome_correntista, saldo=0):
        self.numero_conta = numero_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterar_nome(self, novo_nome):
        self.nome_correntista = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser maior que zero.")

    def saque(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        elif valor <= 0:
            print("O valor do saque deve ser maior que zero.")
        else:
            print("Saldo insuficiente para o saque.")

    def mostrar_informacoes(self):
        print(f"Número da Conta: {self.numero_conta}")
        print(f"Nome do Correntista: {self.nome_correntista}")
        print(f"Saldo Atual: R$ {self.saldo:.2f}")


conta1 = ContaCorrente(numero_conta="12345", nome_correntista="João")

conta1.mostrar_informacoes()


conta1.deposito(1000)


conta1.saque(500)
