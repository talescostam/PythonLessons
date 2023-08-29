tabuleiro = [
            "-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"
            ]

game_on = True

jogador_atual = "X"


def imprime_tabuleiro():
    print(tabuleiro[6] + " | " + tabuleiro[7] + " | " + tabuleiro[8] + "      " + "7|8|9")
    print(tabuleiro[3] + " | " + tabuleiro[4] + " | " + tabuleiro[5] + "      " + "4|5|6")
    print(tabuleiro[0] + " | " + tabuleiro[1] + " | " + tabuleiro[2] + "      " + "1|2|3")


def jogadores():
    print("Escolha qual você quer - X ou O")
    p1 = input("Jogador 1: ")
    if p1 == "X":
        p2 = "O"
        print("Jogador 2: " + p2)
    elif p1 == "O":
        p2 = "X"
        print("Jogador 2: " + p2)
    elif p1 != "O" or p1 != "X":
        print("Invalido. Escolha somente X ou O")
        iniciar_jogo()


def posicao_jogador():
    global jogador_atual
    print("Jogador atual: " + jogador_atual)
    posicao = input("Escolha uma posição de 1 a 9: ")

    valido = False
    while not valido:
        while posicao not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            posicao = input("Escolha uma posição de 1 a 9: ")
        posicao = int(posicao) - 1

        if tabuleiro[posicao] == "-":
            valido = True
        else:
            print("Posição já selecionada, escolha outra posição!")
    tabuleiro[posicao] = jogador_atual
    imprime_tabuleiro()


def iniciar_jogo():
    print("Jogo da velha do Tales")
    imprime_tabuleiro()
    jogadores()


def muda_jogador():
    global jogador_atual
    if jogador_atual == "X":
        jogador_atual = "O"
    else:
        jogador_atual = "X"


iniciar_jogo()
while game_on:
    posicao_jogador()
    muda_jogador()
