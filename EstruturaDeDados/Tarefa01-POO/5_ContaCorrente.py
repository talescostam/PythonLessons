class ContaCorrente:
    def __init__(self, conta, nome, saldo=0):
        self.conta: int = conta
        self.nome: str = nome
        self.saldo: float = saldo

    def alterarNome(self, nomeNovo):
        self.nome = nomeNovo

    def deposito(self, valorDepositado):
        self.saldo += valorDepositado

    def saque(self, valorSacado):
        if valorSacado <= self.saldo:
            self.saldo -= valorSacado
        else:
            return print('Saldo insuficiente')
