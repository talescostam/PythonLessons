# Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista.
# Em seguida, calcule a média anual das temperaturas
# e mostre a média calculada juntamente com todas as temperaturas acima da média anual,
# e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

listaDeTemperaturasNoRJ = [40, 35, 30, 35, 30, 20, 20, 25, 25, 30, 35, 48]

somaTemperaturas = 0
for temperatura in listaDeTemperaturasNoRJ:
    somaTemperaturas += temperatura

mediaAnual = somaTemperaturas / len(listaDeTemperaturasNoRJ)

listaAcimaDaMedia = []
for i in range(1, 13):
    if listaDeTemperaturasNoRJ[i - 1] > mediaAnual:
        listaAcimaDaMedia.append((i, listaDeTemperaturasNoRJ[i - 1]))

dicionarioDeMeses = {
    1: "Jan",
    2: "Fev",
    3: "Mar",
    4: "Abr",
    5: "Mai",
    6: "Jun",
    7: "Jul",
    8: "Ago",
    9: "Set",
    10: "Out",
    11: "Nov",
    12: "Dez"
}

print(f"A média calculada dos meses do ano é: {mediaAnual:.2f}°C")

print("Meses com temperaturas acima da média anual:")
for mes, temperatura in listaAcimaDaMedia:
    print(f"{mes} - {dicionarioDeMeses[mes]}: {temperatura}°C")
