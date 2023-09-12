class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor: str = cor
        self.circunferencia: int = circunferencia
        self.material: str = material

    def trocaCor(self, corNova):
        self.cor = corNova

    def mostraCor(self):
        return print(f'A cor da bola é {self.cor}.')


bola1 = Bola("azul", 2, "plastico")
bola1.mostraCor()
bola1.trocaCor("verde")
bola1.mostraCor()
