# Escreva uma função recursiva que determine quantas vezes um dígito K ocorre em um número natural N.
# Por exemplo, o dígito 2 ocorre 3 vezes em 762021192.

def contar_digitos(n, k):
    # Caso base: quando o número se torna zero, não há mais dígitos para contar
    if n == 0:
        return 0

    # Obtém o último dígito do número
    ultimo_digito = n % 10

    # Verifica se o último dígito é igual a K
    if ultimo_digito == k:
        # Se for igual, incrementa o contador
        return 1 + contar_digitos(n // 10, k)
    else:
        # Se não for igual, continue a busca nos dígitos restantes
        return contar_digitos(n // 10, k)

# Solicitar ao usuário o número N e o dígito K
n = int(input("Digite um número natural N: "))
k = int(input("Digite o dígito K que deseja contar: "))

# Chamar a função para contar o dígito K em N
ocorrencias = contar_digitos(n, k)

# Imprimir o resultado
print(f"O dígito {k} ocorre {ocorrencias} vezes em {n}.")
