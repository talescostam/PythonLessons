class NodoFila:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)


class Fila:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def insere(self, novo_dado):
        novo_nodo = NodoFila(novo_dado)

        if self.primeiro == None:
            self.primeiro = novo_nodo
            self.ultimo = novo_nodo
        else:
            self.ultimo.proximo = novo_nodo
            self.ultimo = novo_nodo

    def remove(self):
        assert self.primeiro != None, "Impossível remover elemento de fila vazia."
        self.primeiro = self.primeiro.proximo

        if self.primeiro == None:
            self.ultimo = None

    def vazia(self):
        return self.primeiro is None

    def busca(self, valor):
        posicao = 0
        corrente = self.primeiro

        while corrente:
            if corrente.dado == valor:
                return posicao
            corrente = corrente.proximo
            posicao += 1

        return -1

    def imprime(self):
        elementos = []
        corrente = self.primeiro

        while corrente:
            elementos.append(str(corrente.dado))
            corrente = corrente.proximo

        print("Fila:", " -> ".join(elementos))

    def inverter(self):
        elementos = []
        corrente = self.primeiro

        while corrente:
            elementos.append(corrente.dado)
            corrente = corrente.proximo

        for elemento in reversed(elementos):
            self.insere(elemento)


fila1 = Fila()
fila1.insere(1)
fila1.insere(2)
fila1.insere(3)
print("Fila: ", fila1)

fila1.remove()
print("Fila após remoção: ", fila1)

fila1.insere(4)
print("Fila após inserção: ", fila1)

print("A fila está vazia?", fila1.vazia())

fila2 = Fila()
fila2.insere(1)
fila2.insere(2)
fila2.insere(3)
fila2.insere(4)
fila2.insere(5)

valor = 3
posicao = fila2.busca(valor)
if posicao >= 0:
    print(f"O valor {valor} está na posição {posicao} na fila.")
else:
    print(f"O valor {valor} não foi encontrado na fila.")

fila2.imprime()

fila2.inverter()
fila2.imprime()
