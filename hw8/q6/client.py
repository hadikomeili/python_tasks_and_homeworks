
import socket

s = socket.socket()
port = 8000
ip = '127.0.0.1'
s.connect((ip, port))
print('Translate is DONE')
while True:
    message = input('Enter Text For Translate :\n')
    s.send(message.encode())
    res = s.recv(2048).decode()
    print(res)