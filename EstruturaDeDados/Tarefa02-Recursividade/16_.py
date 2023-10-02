# A função fatorial duplo é definida como o produto de todos os números naturais ímpares
# de 1 até algum número natural ímpar N. Assim, o fatorial duplo de 5 é 5!! = 1 * 3 * 5 = 15
# Faça uma função recursiva que receba um número inteiro positivo impar N e retorne o fatorial duplo desse número.

def fatorial_duplo(N):
    if N == 1:
        return 1
    return N * fatorial_duplo(N - 2)


N = int(input("Digite um número inteiro positivo ímpar N: "))
if N % 2 == 0:
    print("O número digitado não é ímpar.")
else:
    resultado = fatorial_duplo(N)
    print(f"O fatorial duplo de {N} é {resultado}.")
