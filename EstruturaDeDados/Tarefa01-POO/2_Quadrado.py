class Quadrado:
    def __init__(self, tamanhoDoLado):
        self.lado: int = tamanhoDoLado

    def setLado(self, novoTamanhoDoLado):
        self.lado = novoTamanhoDoLado

    def getLado(self):
        return print(f'O lado do quadrado é {self.lado}cm.')

    def calcularArea(self):
        return print(f'A área do quadrado que tem {self.lado}cm de lado é: {self.lado * self.lado}cm².')


quadrado1 = Quadrado(5)
quadrado1.getLado()
quadrado1.calcularArea()

quadrado1.setLado(4)
quadrado1.getLado()
quadrado1.calcularArea()
