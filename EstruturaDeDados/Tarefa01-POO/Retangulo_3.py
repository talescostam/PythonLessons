class Retangulo_3:
    def __init__(self, base, altura):
        self.base: int = base
        self.altura: int = altura

    def setLado(self, qualLado, valorLado):
        if qualLado == 'base':
            self.base = valorLado
        elif qualLado == 'altura':
            self.altura = valorLado
        else:
            return print('Escolha apenas entre "base" ou "altura".')

    def getLados(self):
        return print(f'O valor da base é {self.base}cm e a altura é {self.altura}cm.')

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return (self.base * 2) + (self.altura * 2)
