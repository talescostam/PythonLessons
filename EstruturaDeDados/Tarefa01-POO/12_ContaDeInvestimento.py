class ContaInvestimento:
    def __init__(self, conta, nome, saldoInicial, taxaDeJuros):
        self.conta: int = conta
        self.nome: str = nome
        self.saldo: float = saldoInicial
        self.taxaDeJuros: float = taxaDeJuros

    def adicioneJuros(self):
        self.saldo += (self.taxaDeJuros * self.saldo)


contaPsyBank = ContaInvestimento(1, "José", 1000.0, 0.10)
contaPsyBank.adicioneJuros()
contaPsyBank.adicioneJuros()
contaPsyBank.adicioneJuros()
contaPsyBank.adicioneJuros()
contaPsyBank.adicioneJuros()
print(contaPsyBank.saldo)
