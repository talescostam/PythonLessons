# A função fatorial duplo é definida como o produto de todos os números naturais ímpares
# de 1 até algum número natural ímpar N. Assim, o fatorial duplo de 5 é 5!! = 1 * 3 * 5 = 15
# Faça uma função recursiva que receba um número inteiro positivo impar N e retorne o fatorial duplo desse número.

def fatorial_duplo(N):
    # Caso base: se N for 1, o fatorial duplo é 1
    if N == 1:
        return 1
    # Caso recursivo: o fatorial duplo de N é N multiplicado pelo fatorial duplo de N-2
    return N * fatorial_duplo(N - 2)

# Solicitar ao usuário um número inteiro positivo ímpar N
N = int(input("Digite um número inteiro positivo ímpar N: "))

# Verificar se o número é ímpar
if N % 2 == 0:
    print("O número digitado não é ímpar.")
else:
    # Chamar a função para calcular o fatorial duplo e imprimir o resultado
    resultado = fatorial_duplo(N)
    print(f"O fatorial duplo de {N} é {resultado}.")
