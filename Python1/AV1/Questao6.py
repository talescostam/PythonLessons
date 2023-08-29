print("Combustível    Código")
print("Gasolina       1")
print("Álcool         2")
print("Diesel         3")
print("Fim            4\n")

cbc = 0
contadorDeGasolina = 0
contadorDeAlcool = 0
contadorDeDiesel = 0
while cbc != 1 or cbc != 2 or cbc != 3 or cbc != 4:
    cdc = int(input("Digite aqui o codigo do que vc acabou de usar: "))
    if cdc == 1:
        contadorDeGasolina += 1
    elif cdc == 2:
        contadorDeAlcool = contadorDeAlcool + 1
    elif cdc == 3:
        contadorDeDiesel += 1
    elif cdc == 4:
        print("MUITO OBRIGADO")
        print(f"Gasolina: {contadorDeGasolina}")
        print(f"Alcool: {contadorDeAlcool}")
        print(f"Diesel: {contadorDeDiesel}")
        break
