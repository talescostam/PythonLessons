# Faça uma função recursiva que receba um número inteiro positivo par N
# e imprima todos os números pares de 0 até N em ordem decrescente.

def imprimir_pares_decrescente(n):
    if n < 0:
        return
    if n % 2 == 0:
        print(n)
    imprimir_pares_decrescente(n - 1)


n = int(input("Digite um número inteiro positivo par N: "))
if n % 2 != 0:
    print("O número digitado não é par.")
else:
    imprimir_pares_decrescente(n)
