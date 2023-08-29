idade = 0
contadorDeQuantidadeDeIdade = 0
somaDeIdades = 0
while idade >= 0:
    idade = int(input("Insira uma idade: "))
    if idade >= 0:
        contadorDeQuantidadeDeIdade += 1
        somaDeIdades += idade
media = somaDeIdades / contadorDeQuantidadeDeIdade
print(f"A média aritmética dessas idades é: {media:.2f}")
