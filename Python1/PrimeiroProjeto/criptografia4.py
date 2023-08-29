#Desafio da mensagem do Professor
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


mensagem_cifrada = "Imsflg esak ljstsdzgr esak kgjlw lwfzgt Jgtwjlg"

for chave in range(1, 21):
    mensagem_decifrada = decifrar_mensagem(mensagem_cifrada, chave)
    print(f"Chave {chave}: {mensagem_decifrada}")

#chave 18: Quanto mais trabalhoz mais sorte tenhob Roberto