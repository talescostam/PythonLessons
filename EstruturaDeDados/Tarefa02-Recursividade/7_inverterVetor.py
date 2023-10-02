# Crie um programa em python que receba um vetor de números reais com 100 elementos.
# Escreva uma função recursiva que inverta ordem dos elementos presentes no vetor.

def inverterVetor(vetor, inicio, fim):
    if inicio < fim:
        vetor[inicio], vetor[fim] = vetor[fim], vetor[inicio]
        inverterVetor(vetor, inicio + 1, fim - 1)

vetor = list(range(1, 101))
inverterVetor(vetor, 0, len(vetor) - 1)
print("Vetor Invertido: ", vetor)
