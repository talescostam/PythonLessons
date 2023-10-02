# A multiplicação de dois números inteiros pode ser feita através de somas sucessivas.
# Proponha um algoritmo recursivo Multip_Rec(n1,n2) que calcule a multiplicação de dois inteiros.

def multip_rec(n1, n2):
    if n1 == 0 or n2 == 0:
        return 0

    if n1 > 0:
        return n1 + multip_rec(n1, n2 - 1)
    else:
        return -(multip_rec(-n1, n2 - 1))


n1 = int(input("Digite o 1º número inteiro (n1): "))
n2 = int(input("Digite o 2º número inteiro (n2): "))

resultado = multip_rec(n1, n2)

print(f"A multiplicação de {n1} e {n2} é {resultado}.")
