# Crie uma função recursiva que receba um número inteiro positivo N e calcule o produtório dos números de 1 a N.

def somatorio(n: int) -> int:
    if n <= 1:
        return n
    return n * somatorio(n - 1)


print(somatorio(4))
