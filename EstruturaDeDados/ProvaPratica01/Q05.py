# 5) Crie um estudo de caso (cenário)
# e implemente uma das estruturas de dados (Lista, Fila, Pilha - como estruturas ligadas)
# - Descreva o cenário
# - Descreva  a solução
# - Implemente o código
# - Crie uma função main para execução do caso de teste (exemplo)

class BarraDeVidaMinecraft:
    def __init__(self):
        self.vida = []

    def ganharVida(self):
        self.vida.append('♥')

    def perderVida(self):
        if not self.vida:
            print("Sem unidades de vida para remover.")
        else:
            self.vida.pop()

    def verBarraDeVida(self):
        print("Barra de Vida:", "".join(self.vida))


def main():
    barraDeVidaDoPlayer = BarraDeVidaMinecraft()

    for i in range(10):
        barraDeVidaDoPlayer.ganharVida()

    barraDeVidaDoPlayer.verBarraDeVida()

    barraDeVidaDoPlayer.perderVida()
    barraDeVidaDoPlayer.perderVida()

    barraDeVidaDoPlayer.verBarraDeVida()


if __name__ == "__main__":
    main()
