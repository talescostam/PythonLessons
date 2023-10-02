# Faça uma função recursiva que receba um número inteiro positivo par N
# e imprima todos os números pares de 0 até N em ordem crescente.

def imprimirParesCrescente(n):
    if n == 0:
        print(n)
    else:
        if n % 2 == 0:
            print(n)
        imprimirParesCrescente(n - 1)


n = int(input("Digite um número inteiro positivo par: "))
if n % 2 != 0:
    print("O número digitado não é par.")
else:
    imprimirParesCrescente(n)
