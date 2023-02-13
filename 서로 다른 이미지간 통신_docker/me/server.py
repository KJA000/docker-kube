import socket

HOST = socket.gethostbyname('localhost')
PORT = 65456  
dog = "∪･ω･∪"
cat = "(=^･ω･^=)"
bear = "(ó㉨ò)"
rabbit = "／(=´x`=)＼"
pig = "(▼￣⚇￣▼)"
chick = "(・Θ・)"
errormsg = "please type animal !"
print('> echo-server is activated')
#print(HOST,PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as serverSocket:
    serverSocket.bind(('', PORT))
    serverSocket.listen()
    clientSocket, clientAddress = serverSocket.accept()
    with clientSocket:
        print('> client connected by IP address {0} with Port number {1}'.format(clientAddress[0], clientAddress[1]))
        while True:
            # [=start=]
            RecvData = clientSocket.recv(1024)
            if RecvData.decode('utf-8') == 'dog' or RecvData.decode('utf-8') == 'cat' or  RecvData.decode('utf-8') =='bear' or  RecvData.decode('utf-8') =='rabbit' or  RecvData.decode('utf-8') =='pig' or  RecvData.decode('utf-8') =='chick':
                print('> echoed:', RecvData.decode('utf-8'))
            if RecvData.decode('utf-8') == 'quit':
                break
            elif RecvData.decode('utf-8') == 'dog':
                clientSocket.sendall(dog.encode('utf-8'))
            elif RecvData.decode('utf-8') == 'cat':
                clientSocket.sendall(cat.encode('utf-8'))
            elif RecvData.decode('utf-8') == 'bear':
                clientSocket.sendall(bear.encode('utf-8'))
            elif RecvData.decode('utf-8') == 'rabbit':
                clientSocket.sendall(rabbit.encode('utf-8'))
            elif RecvData.decode('utf-8') == 'pig':
                clientSocket.sendall(pig.encode('utf-8'))
            elif RecvData.decode('utf-8') == 'chick':
                clientSocket.sendall(chick.encode('utf-8'))
            else:
                clientSocket.sendall(errormsg.encode('utf-8'))
                print('> echoed:', RecvData.decode('utf-8'), " - not animal")
            #clientSocket.sendall(RecvData)
            # [==end==]
print('> echo-server is de-activated')
