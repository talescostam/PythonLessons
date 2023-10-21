class NodoLista:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def adicionarNodoInicio(self, lista, valor):
        novoNodo = NodoLista(valor, lista.cabeca)
        lista.cabeca = novoNodo

    def adicionarNodoFinal(self, lista, nodo_anterior, novo_dado):
        novoNodo = NodoLista(novo_dado)
        novoNodo.proximo = nodo_anterior.proximo
        nodo_anterior.proximo = novoNodo

    def busca(self, lista, valor):
        corrente = lista.cabeca
        while corrente and corrente.dado != valor:
            corrente = corrente.proximo
        return corrente

    def remove(self, lista, valor):
        anterior = None
        corrente = lista.cabeca

        while corrente and corrente.dado != valor:
            anterior = corrente
            corrente = corrente.proximo

        if corrente:
            if anterior:
                anterior.proximo = corrente.proximo
            else:
                lista.cabeca = corrente.proximo

        return corrente

    def removerDuplicatas(self):
        corrente = self.cabeca
        while corrente and corrente.proximo:
            if corrente.dado == corrente.proximo.dado:
                corrente.proximo = corrente.proximo.proximo
            else:
                corrente = corrente.proximo


class TesteListaEncadeada:
    lista = ListaEncadeada()
    print("Lista vazia: ", lista)

    lista.adicionarNodoInicio(lista, 3)
    lista.adicionarNodoInicio(lista, 3)
    lista.adicionarNodoInicio(lista, 3)
    print("Lista contém 3 elemento iguais: ", lista)

    lista.removerDuplicatas()
    print("Lista com apenas um '3': ", lista)
    nodo_anterior = lista.cabeca
    lista.adicionarNodoFinal(lista, nodo_anterior, 10)
    print("Inserindo um novo elemento depois de um outro: ", lista)

    for i in range(8):
        lista.adicionarNodoInicio(lista, i)
    print("Lista: ", lista)

    lista.remove(lista, 4)

    for i in range(8, -4, -2):
        elemento = lista.busca(lista, i)
        if elemento:
            print("Elemento {0} presente na lista!".format(i))
        else:
            print("Elemento {0} não encontrado.".format(i))
