import socket
import pickle
import random
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host = '127.0.0.1'
Port = 55555
server.bind((Host, Port))

server.listen()
user, address = server.accept()
user.send('начинаем работу!'.encode('utf-8'))
print("получаю Агп...")
A_g_p = user.recv(1024).decode('utf-8')

A = int(A_g_p[0])
g = int(A_g_p[1])
p = int(A_g_p[2])

print('генерирую В...')
b = random.randint(10, 20)
B = g ** b % p

print('отправляю В...')
user.send(str(B).encode('utf-8'))

K = A**b % p
print('Полученное число К: ', K)

while True:

    print('**Введите сообщение для клиента:** ')
    #user.send('Вы подключены'.encode('utf-8'))
    user.send(input().encode('utf-8'))
    data = user.recv(1024)
    print(data.decode('utf-8'))
    if data.decode('utf-8') == 'exit':
        break
