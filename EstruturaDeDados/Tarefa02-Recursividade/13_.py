# Faça uma função recursiva que receba um número inteiro positivo N
# e imprima todos os números naturais de 0 até N em ordem decrescente.

def imprimir_naturais_decrescente(n):
    if n == 0:
        print(n)
    else:
        print(n)
        imprimir_naturais_decrescente(n - 1)


n = int(input("Digite um número inteiro positivo N: "))
imprimir_naturais_decrescente(n)
