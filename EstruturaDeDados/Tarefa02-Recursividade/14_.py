# Faça uma função recursiva que receba um número inteiro positivo par N
# e imprima todos os números pares de 0 até N em ordem crescente.

def imprimir_pares_crescente(n):
    # Caso base: quando n chega a 0, não imprime mais nada
    if n == 0:
        print(n)
    else:
        # Se o número atual for par, imprima-o
        if n % 2 == 0:
            print(n)
        # Faça uma chamada recursiva com o número anterior
        imprimir_pares_crescente(n - 1)

# Solicitar ao usuário um número inteiro positivo par N
n = int(input("Digite um número inteiro positivo par N: "))

# Verificar se o número é par
if n % 2 != 0:
    print("O número digitado não é par.")
else:
    # Chamar a função para imprimir os números pares em ordem crescente
    imprimir_pares_crescente(n)