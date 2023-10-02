# Faça uma função recursiva que receba um número inteiro positivo N
# e imprima todos os números naturais de 0 até N em ordem decrescente.

def imprimir_naturais_decrescente(n):
    # Caso base: quando n chega a 0, não imprime mais nada
    if n == 0:
        print(n)
    else:
        # Imprime o número atual (decrementando em cada chamada)
        print(n)
        imprimir_naturais_decrescente(n - 1)

# Solicitar ao usuário um número inteiro positivo N
n = int(input("Digite um número inteiro positivo N: "))

# Chamar a função para imprimir os números naturais em ordem decrescente
imprimir_naturais_decrescente(n)
