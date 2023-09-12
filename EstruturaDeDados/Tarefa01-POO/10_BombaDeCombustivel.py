class BombaDeCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel: str = tipoCombustivel
        self.valorLitro: float = valorLitro
        self.quantidadeCombustivel: float = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        quantidadeAbastecido = valor / self.valorLitro
        if quantidadeAbastecido <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= quantidadeAbastecido
            return print(f'Com {valor}Reais o veículo abasteceu {quantidadeAbastecido}L')
        else:
            return print(f'Quantidade de combustivel disponível é de apenas: {self.quantidadeCombustivel}')

    def abastecerPorLitro(self, litro):
        valorAbastecido = litro * self.valorLitro
        if litro <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litro
            return print(f'{litro}L custou {valorAbastecido} Reais')
        else:
            return print(f'Quantidade de combustivel disponível é de apenas: {self.quantidadeCombustivel}')

    def alterarValor(self, novoValorDoLitro):
        self.valorLitro = novoValorDoLitro

    def alterarCombustivel(self, novoCombustivel):
        self.tipoCombustivel = novoCombustivel

    def alterarQuantidadeCombustivel(self, novaQuantidade):
        self.quantidadeCombustivel = novaQuantidade
