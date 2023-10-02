# Faça uma função recursiva que receba um número inteiro positivo N
# e imprima todos os números naturais de 0 até N em ordem crescente.

def imprimir_naturais_crescente(n):
    # Caso base: quando n chega a 0, não imprime mais nada
    if n == 0:
        print(n)
    else:
        # Imprime o número atual (decrementando em cada chamada)
        imprimir_naturais_crescente(n - 1)
        print(n)

# Solicitar ao usuário um número inteiro positivo N
n = int(input("Digite um número inteiro positivo N: "))

# Chamar a função para imprimir os números naturais
imprimir_naturais_crescente(n)
