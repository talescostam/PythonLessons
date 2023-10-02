# Escreva uma função recursiva que determine quantas vezes um dígito K ocorre em um número natural N.
# Por exemplo, o dígito 2 ocorre 3 vezes em 762021192.

def contarDigitos(n, numeroParaContar):
    if n == 0:
        return 0

    ultimo_digito = n % 10

    if ultimo_digito == numeroParaContar:
        return 1 + contarDigitos(n // 10, numeroParaContar)
    else:
        return contarDigitos(n // 10, numeroParaContar)


n = int(input("Digite um número natural: "))
numeroParaContar = int(input("Qual número você quer ver a quantidade de repetição: "))
quantidadeTotal = contarDigitos(n, numeroParaContar)
print(f"O dígito {numeroParaContar} se repete {quantidadeTotal} vezes em {n}.")
