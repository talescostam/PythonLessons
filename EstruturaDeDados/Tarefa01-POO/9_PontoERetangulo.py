class Ponto:
    def __init__(self, x, y):
        self.x: int = x
        self.y: int = y
        self.coordenada: list = [self.x, self.y]

    def getPontos(self):
        return self.coordenada


class Retangulo:
    def __init__(self, base, altura):
        self.base: int = base
        self.altura: int = altura
        self.verticeDePartida: Ponto = Ponto(0, 0)

    def encontrarCentro(self):
        x = self.base/2
        y = self.altura/2
        centro = Ponto(x, y)
        return print(f'O centro do retângulo de base {self.base} e altura {self.altura} é: {centro.getPontos()}')

    def setLado(self, qualLado, valorLado):
        if qualLado == 'base':
            self.base = valorLado
        elif qualLado == 'altura':
            self.altura = valorLado
        else:
            return print('Escolha apenas entre "base" ou "altura".')


retangulo1 = Retangulo(4, 6)
retangulo1.encontrarCentro()
retangulo2 = Retangulo(6, 6)
retangulo2.encontrarCentro()
retangulo3 = Retangulo(8, 4)
retangulo3.encontrarCentro()

retangulo3.setLado("base", 4)
retangulo3.encontrarCentro()
