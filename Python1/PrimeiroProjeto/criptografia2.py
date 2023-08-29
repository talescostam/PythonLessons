#Desafio 2
def cifrar_mensagem(mensagem):
    mensagem_cifrada = ''
    for caractere in mensagem:
        if caractere.isalpha():
            base = ord('a') if caractere.islower() else ord('A')
            novo_caractere = chr((ord(caractere) - base + 5) % 26 + base)
            mensagem_cifrada += novo_caractere
        elif caractere.isdigit():
            novo_digito = str((int(caractere) + 5) % 10)
            mensagem_cifrada += novo_digito
        else:
            mensagem_cifrada += caractere
    return mensagem_cifrada

def decifrar_mensagem(mensagem_cifrada):
    mensagem_decifrada = ''
    for caractere in mensagem_cifrada:
        if caractere.isalpha():
            base = ord('a') if caractere.islower() else ord('A')
            novo_caractere = chr((ord(caractere) - base - 5) % 26 + base)
            mensagem_decifrada += novo_caractere
        elif caractere.isdigit():
            novo_digito = str((int(caractere) - 5) % 10)
            mensagem_decifrada += novo_digito
        else:
            mensagem_decifrada += caractere
    return mensagem_decifrada

mensagem_original = "A d z 0 9"
mensagem_cifrada = cifrar_mensagem(mensagem_original)
print("Mensagem cifrada:", mensagem_cifrada)

mensagem_decifrada = decifrar_mensagem(mensagem_cifrada)
print("Mensagem decifrada:", mensagem_decifrada)

mensagem_original = "Boa noite, Professor! Eu fiz uma criptografia muito legal!"
mensagem_cifrada = cifrar_mensagem(mensagem_original)
print("Mensagem cifrada:", mensagem_cifrada)

mensagem_decifrada = decifrar_mensagem(mensagem_cifrada)
print("Mensagem decifrada:", mensagem_decifrada)

