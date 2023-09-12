class Carro:
    def __init__(self, consumo):
        self.consumo: int = consumo
        self.tanque: int = 0

    def andar(self, km):
        tanqueGasto = km / self.consumo
        if tanqueGasto > self.tanque:
            self.tanque = 0
            print('O veículo parou no meio da estrada sem gasolina')
        else:
            self.tanque -= tanqueGasto

    def obterGasolina(self):
        return print(f'{self.tanque}')

    def adicionarGasolina(self, gasolinaNova):
        self.tanque += gasolinaNova


meuFusca = Carro(15)
meuFusca.adicionarGasolina(20)
meuFusca.andar(100)
meuFusca.obterGasolina()
