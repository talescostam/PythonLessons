# Faça uma função recursiva que receba um número inteiro positivo par N
# e imprima todos os números pares de 0 até N em ordem crescente.

def imprimir_pares_crescente(n):
    if n == 0:
        print(n)
    else:
        if n % 2 == 0:
            print(n)
        imprimir_pares_crescente(n - 1)


n = int(input("Digite um número inteiro positivo par N: "))
if n % 2 != 0:
    print("O número digitado não é par.")
else:
    imprimir_pares_crescente(n)
