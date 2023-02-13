import socket

HOST = '127.0.0.3'

#포트넘버 서버와 같은 것으로 수정
PORT = 65456

print('> echo-client is activated')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
    print(HOST,PORT) 
    clientSocket.connect((HOST, PORT))
    print("<connectd> type your favorit animal !\n 1.dog 2.cat 3.rabbit 4.bear 5.pig 6.chick ")
    while True:
        sendMsg = input()
        clientSocket.sendall(bytes(sendMsg, 'utf-8'))
        recvData = clientSocket.recv(1024)
        print('> received:', recvData.decode('utf-8'))
        if sendMsg == "quit":
            break

print('> echo-client is de-activated')
