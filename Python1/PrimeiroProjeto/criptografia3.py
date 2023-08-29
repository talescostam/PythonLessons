#Desafio 3

def cifrar_mensagem(mensagem, chave):
    mensagem_cifrada = ''
    for caractere in mensagem:
        if caractere.isalpha():
            base = ord('a') if caractere.islower() else ord('A')
            novo_caractere = chr((ord(caractere) - base + chave) % 26 + base)
            mensagem_cifrada += novo_caractere
        elif caractere.isdigit():
            novo_digito = str((int(caractere) + chave) % 10)
            mensagem_cifrada += novo_digito
        else:
            mensagem_cifrada += caractere
    return mensagem_cifrada


def decifrar_mensagem(mensagem_cifrada, chave):
    mensagem_decifrada = ''
    for caractere in mensagem_cifrada:
        if caractere.isalpha():
            base = ord('a') if caractere.islower() else ord('A')
            novo_caractere = chr((ord(caractere) - base - chave) % 26 + base)
            mensagem_decifrada += novo_caractere
        elif caractere.isdigit():
            novo_digito = str((int(caractere) - chave) % 10)
            mensagem_decifrada += novo_digito
        else:
            mensagem_decifrada += caractere
    return mensagem_decifrada


chave = int(input("Digite a chave de cifragem: "))

mensagem_original = "A d z 0 9"
mensagem_cifrada = cifrar_mensagem(mensagem_original, chave)
print("Mensagem cifrada:", mensagem_cifrada)

mensagem_decifrada = decifrar_mensagem(mensagem_cifrada, chave)
print("Mensagem decifrada:", mensagem_decifrada)

mensagem_original = "Boa noite, Professor! Eu fiz uma criptografia muito legal!"
mensagem_cifrada = cifrar_mensagem(mensagem_original, chave)
print("Mensagem cifrada:", mensagem_cifrada)

mensagem_decifrada = decifrar_mensagem(mensagem_cifrada, chave)
print("Mensagem decifrada:", mensagem_decifrada)
