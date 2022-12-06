import socket
import random

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

a = random.randint(10, 20)
p, g = 7, 5
A = g ** a % p
A_g_p = str(A)+str(g)+str(p)#[A, g, p]
print(A_g_p)
print(client.recv(1024).decode('utf-8'))

print('посылаю Агп на сервер...')
client.send(A_g_p.encode('utf-8'))

print("получаю B...")
B = client.recv(1024).decode('utf-8')

K = int(B)**a % p
print('Полученное число К: ', K)

while True:

    data = client.recv(1024)
    print(data.decode('utf-8'))
    print('**Введите сообщение для сервера:** ')
    message = input().encode('utf-8')
    client.send(message)
    if message == 'exit':
        break
