# Faça uma função recursiva que receba um número inteiro positivo N
# e imprima todos os números naturais de 0 até N em ordem crescente.

def imprimiNaturaisCrescente(n):
    if n == 0:
        print(n)
    else:
        imprimiNaturaisCrescente(n - 1)
        print(n)


n = int(input("Digite um número inteiro positivo N: "))
imprimiNaturaisCrescente(n)
