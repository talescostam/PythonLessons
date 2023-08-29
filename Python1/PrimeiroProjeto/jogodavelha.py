jogadaAtual = 1
tab = [" "*3, " "*3, " "*3]
def imprimeTabuleiro():
    tab = [" "*3, " "*3, " "*3]
    for i in range(3):
        print('       |       |       ')
        print(f'   {tab[i][0]}   |   {tab[i][1]}   |   {tab[i][2]}   ')
        if i == 2:
            print('       |       |       ')
        else:
            print('_______|_______|_______')

def rodada():
    jogada = 1
    if jogada % 2 != 0:
        i = input("Jogador 1, joga ai a linha: ")
        j = input("Jogador 1, joga ai a coluna: ")
        tab[i][j] = "X"
    else:
        i = input("Jogador 2, joga ai a linha: ")
        j = input("Jogador 2, joga ai a coluna: ")
        tab[i][j] = "O"
    jogada += jogada

while jogadaAtual < 10:
    imprimeTabuleiro()
    rodada()
    jogadaAtual = jogada

imprimeTabuleiro()
print("fim de jogo")