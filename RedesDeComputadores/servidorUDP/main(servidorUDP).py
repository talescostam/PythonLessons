import socket  # Importa o módulo socket

localIP = "127.0.0.1"  # IP localhost
localPort = 20001
bufferSize = 1024
# Cria um socket UDP
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Vincula o socket a um IP e Porta
UDPServerSocket.bind((localIP, localPort))
print("Servidor UDP está ligado e ouvindo")
# Espera por datagramas que chegam
while True:
    message, address = UDPServerSocket.recvfrom(bufferSize)
    print("Message from Client:{}".format(message))
    print("Client IP Address:{}".format(address))
    # Re-envie a mensagem modificada ao cliente
    bytesToSend = message.upper()
    UDPServerSocket.sendto(bytesToSend, address)
