# 4) Faça uma função recursiva que permita somar os elementos de um vetor de inteiros.

def somaVetor(lista):
    if not lista:  # É a mesma coisa que "if lista == []:"
        return 0
    return lista[0] + somaVetor(lista[1:])


vetor = [1, 2, 3]
print(somaVetor(vetor))
