class TamagoshiPlus:
    def __init__(self, nome, fome=0, saude=10, idade=0):
        self.nome: str = nome
        self.fome: int = fome
        self.saude: int = saude
        self.idade: int = idade
        self.humor: str = self.getHumor()

    def __str__(self):
        return

    def setNome(self, novoNome):
        self.nome = novoNome

    def setFome(self, novaFome):
        self.fome = novaFome

    def setSaude(self, novaSaude):
        self.saude = novaSaude

    def setIdade(self, novaIdade):
        self.idade = novaIdade

    def getNome(self):
        return self.nome

    def getFome(self):
        return self.fome

    def getSaude(self):
        return self.saude

    def getIdade(self):
        return self.idade

    def getHumor(self):
        if self.fome < 5 < self.saude:
            self.humor = "feliz"
        else:
            self.humor = "triste"
        return self.humor


class FazendaDeBichinhos:
    def __init__(self):
        self.listaDeBichinhos: list = []

    def adicionaBichosNaFazenda(self, bicho):
        self.listaDeBichinhos.append(bicho)


tama1 = TamagoshiPlus("Geraldo")
tama2 = TamagoshiPlus("名")
tama3 = TamagoshiPlus("Catarina")

fazendaFeliz = FazendaDeBichinhos()
fazendaFeliz.adicionaBichosNaFazenda(tama1)
fazendaFeliz.adicionaBichosNaFazenda(tama2)
fazendaFeliz.adicionaBichosNaFazenda(tama3)

