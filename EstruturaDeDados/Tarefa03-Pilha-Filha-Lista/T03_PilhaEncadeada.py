class NodoPilha:
    def __init__(self, dado=0, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)

class Pilha:
    def __init__(self):
        self.topo = None

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def insere(self, novo_dado):
        novo_nodo = NodoPilha(novo_dado)
        novo_nodo.anterior = self.topo
        self.topo = novo_nodo

    def remove(self):
        assert self.topo, "Impossível remover valor de pilha vazia."
        self.topo = self.topo.anterior

    def maiorElementoDaPilha(self, pilha):
        if not pilha.topo:
            return None

        maior = pilha.topo.dado
        nodo_atual = pilha.topo

        while nodo_atual:
            if nodo_atual.dado > maior:
                maior = nodo_atual.dado
            nodo_atual = nodo_atual.anterior

        return maior

    def imprimirNaOrdemInversa(self):
        nodo_atual = self.topo
        while nodo_atual:
            print(nodo_atual.dado, end=' -> ')
            nodo_atual = nodo_atual.anterior
        print("None")

    def compararIgualdadeDePilha(self, outra_pilha):
        nodo1 = self.topo
        nodo2 = outra_pilha.topo

        while nodo1 and nodo2:
            if nodo1.dado != nodo2.dado:
                print("Diferente")
                return False
            nodo1 = nodo1.anterior
            nodo2 = nodo2.anterior

        if nodo1 is None and nodo2 is None:
            print("Igual")
            return True
        else:
            print("Diferente")
            return False

    def tPilha(self, vetor):
        for numero in vetor:
            if numero % 2 == 0:
                self.insere(numero)
            else:
                numeroRetirado = self.topo.dado if self.topo else None
                if numeroRetirado is not None:
                    print(f"Retirado da pilha: {numeroRetirado}")

        while self.topo:
            numeroRetirado = self.topo.dado
            print(f"Retirado da pilha: {numeroRetirado}")
            self.remove()

    def tPilha2(self, outra_pilha, vetor):
        for numero in vetor:
            if numero > 0:
                self.insere(numero)
            elif numero < 0:
                outra_pilha.insere(numero)
            else:
                elemento_atual = self.topo.dado if self.topo else None
                elemento_outra_pilha = outra_pilha.topo.dado if outra_pilha.topo else None
                if elemento_atual is not None:
                    print(f"Retirado da pilha atual: {elemento_atual}")
                    self.remove()
                if elemento_outra_pilha is not None:
                    print(f"Retirado da outra pilha: {elemento_outra_pilha}")
                    outra_pilha.remove()


class TestePilha:
    pilha1 = Pilha()
    pilha1.insere(3)
    pilha1.insere(4)
    pilha1.insere(5)
    pilha1.insere(2)
    pilha1.insere(1)

    maior = pilha1.maiorElementoDaPilha(pilha1)
    print("Maior elemento na pilha:", maior)
    pilha1.imprimirNaOrdemInversa()

    pilha2 = Pilha()
    pilha2.insere(3)
    pilha2.insere(4)
    pilha2.insere(5)
    pilha2.insere(2)
    pilha2.insere(1)

    pilha3 = Pilha()
    pilha3.insere(1)

    pilha1.compararIgualdadeDePilha(pilha2)
    pilha1.compararIgualdadeDePilha(pilha3)

    vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    pilhaT = Pilha()
    pilhaT.tPilha(vetor)

    vetor = [1, 2, 0, -3, -4, 0, 5, -6]
    minhaPilha = Pilha()
    outraPilha = Pilha()
    minhaPilha.tPilha2(outraPilha, vetor)

class PilhaCarros:
    def __init__(self):
        self.carros = []

    def estacionarCarro(self, placa):
        self.carros.append(placa)

    def verificarEstacionamento(self, placa):
        sequencia = []
        temCarro = False

        while self.carros:
            carro = self.carros.pop()
            sequencia.append(carro)

            if carro == placa:
                temCarro = True
                break

        if temCarro:
            print(f"O carro {placa} consegue sair. Retire nessa ordem: {sequencia}")
        else:
            print(f"O carro {placa} não foi encontrado na rua.")


pilhaCarros = PilhaCarros()

pilhaCarros.estacionarCarro("12345")
pilhaCarros.estacionarCarro("67890")
pilhaCarros.estacionarCarro("54321")

placaDesejada = "67890"
pilhaCarros.verificarEstacionamento(placaDesejada)
