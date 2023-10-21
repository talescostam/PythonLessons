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


class Processo:
    def __init__(self, id, tempoDeEspera):
        self.id = id
        self.tempoDeEspera = tempoDeEspera

    def __repr__(self):
        return f"Processo {self.id} (Tempo de Espera: {self.tempoDeEspera})"


class Fila:
    def __init__(self):
        self.processos = []

    def __repr__(self):
        return "[" + str(self.processos) + "]"

    def adicionarProcesso(self, processo):
        self.processos.append(processo)

    def matarProcesso(self):
        if not self.processos:
            return None

        processo_mais_longo = max(self.processos, key=lambda p: p.tempoDeEspera)
        self.processos.remove(processo_mais_longo)
        return processo_mais_longo

    def executarProcesso(self):
        if not self.processos:
            return None

        processo_executado = self.processos.pop(0)
        return processo_executado


filaDeProcessos = Fila()
filaDeProcessos.adicionarProcesso(Processo(1, 3))
filaDeProcessos.adicionarProcesso(Processo(2, 2))
filaDeProcessos.adicionarProcesso(Processo(3, 5))

print("Fila de Processos: ")
print(filaDeProcessos)

processoEmExecucao = filaDeProcessos.executarProcesso()
print(f"Processo Executado: {processoEmExecucao}")

print("Fila de Processos após Execução: ")
print(filaDeProcessos)

processoMaisLongo = filaDeProcessos.matarProcesso()
print(f"Processo com maior tempo para morrer: {processoMaisLongo}")

print("Fila de Processos após o kill: ")
print(filaDeProcessos)
