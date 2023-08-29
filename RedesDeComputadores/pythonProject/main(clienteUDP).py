import socket  # importa o módulo socket
serverIP = "127.0.0.1"  # IP localhost
serverPort = 20001
bufferSize = 1024

serverAddressPort = (serverIP, serverPort)  # IP e porta do servidor
msgFromClient = input("Mensagem: ")
bytesToSend = str.encode(msgFromClient)
# Crie um socket UDP
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
# Envie uma mensagem para o servidor
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
# Espere a resposta do servidor
msgFromServer = UDPClientSocket.recvfrom(bufferSize)
print("Message from Server {}".format(msgFromServer[0]))
UDPClientSocket.close()
