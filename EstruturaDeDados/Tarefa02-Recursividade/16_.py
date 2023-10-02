# A função fatorial duplo é definida como o produto de todos os números naturais ímpares
# de 1 até algum número natural ímpar N. Assim, o fatorial duplo de 5 é 5!! = 1 * 3 * 5 = 15
# Faça uma função recursiva que receba um número inteiro positivo impar N e retorne o fatorial duplo desse número.

def fatorialDuplo(n):
    if n == 1:
        return 1
    return n * fatorialDuplo(n - 2)


n = int(input("Digite um número inteiro positivo ímpar: "))
if n % 2 == 0:
    print("O número digitado não é ímpar.")
else:
    resultado = fatorialDuplo(n)
    print(f"O fatorial duplo de {n} é {resultado}.")
