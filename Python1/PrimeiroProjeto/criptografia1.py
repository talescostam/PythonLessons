#Desafio 1
def cifrar(texto):
    tabela_substituicao = {
        'Z': 'P',
        'E': 'O',
        'N': 'L',
        'I': 'A',
        'T': 'R',

    }
    texto_cifrado = ''
    for caractere in texto:
        if caractere.upper() in tabela_substituicao:
            caractere_cifrado = tabela_substituicao[caractere.upper()]
            if caractere.islower():
                caractere_cifrado = caractere_cifrado.lower()
            texto_cifrado += caractere_cifrado
        else:
            texto_cifrado += caractere
    return texto_cifrado


def decifrar(texto_cifrado):
    tabela_substituicao = {
        'P': 'Z',
        'O': 'E',
        'L': 'N',
        'A': 'I',
        'R': 'T'
    }
    texto_decifrado = ''
    for caractere in texto_cifrado:
        if caractere.upper() in tabela_substituicao:
            caractere_decifrado = tabela_substituicao[caractere.upper()]
            if caractere.islower():
                caractere_decifrado = caractere_decifrado.lower()
            texto_decifrado += caractere_decifrado
        else:
            texto_decifrado += caractere
    return texto_decifrado


entrada = "Todo mundo age não apenas por compulsão externa, mas também por necessidade íntima"
saida_cifrada = cifrar(entrada)
print("Saída cifrada:", saida_cifrada)
saida_decifrada = decifrar(saida_cifrada)
print("Saída decifrada:", saida_decifrada)
