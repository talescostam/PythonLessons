# A multiplicação de dois números inteiros pode ser feita através de somas sucessivas.
# Proponha um algoritmo recursivo Multip_Rec(n1,n2) que calcule a multiplicação de dois inteiros.

def multip_rec(n1, n2):
    # Caso base: Se um dos números for zero, o resultado é zero
    if n1 == 0 or n2 == 0:
        return 0

    # Caso recursivo: Se ambos os números são positivos, multiplique um deles por n2-1
    if n1 > 0:
        return n1 + multip_rec(n1, n2 - 1)
    # Caso recursivo: Se n1 for negativo, multiplique -n1 por n2-1 e negue o resultado
    else:
        return -(multip_rec(-n1, n2 - 1))

# Solicitar ao usuário os números inteiros n1 e n2
n1 = int(input("Digite o primeiro número inteiro (n1): "))
n2 = int(input("Digite o segundo número inteiro (n2): "))

# Chamar a função para calcular a multiplicação
resultado = multip_rec(n1, n2)

# Imprimir o resultado
print(f"A multiplicação de {n1} e {n2} é {resultado}.")
