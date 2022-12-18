import socket
import random


def encrypt_message(K, message):
    encrypted_message = ""
    for c in message:
        encrypted_message += chr(ord(c) + K)
    return encrypted_message


def decrypt_message(K, encrypted_message):
    decrypted_message = ""
    for c in encrypted_message:
        decrypted_message += chr(ord(c) - K)
    return decrypted_message


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Host = '127.0.0.1'
Port = 55555
server.bind((Host, Port))

server.listen()
user, address = server.accept()
user.send('Соединение установлено'.encode('utf-8'))

A = int(user.recv(1024).decode('utf-8'))
g = int(user.recv(1024).decode('utf-8'))
p = int(user.recv(1024).decode('utf-8'))

# Генерирую b
b = random.randint(1000, 10000)
B = (g ** b) % p

# Отправляю В
user.send(str(B).encode('utf-8'))

K = (A**b) % p
print('Полученное число К: ', K)

while True:

    print('**Введите сообщение для клиента:** ', end='')

    message = str(input().encode('utf-8'))

    encrypted_message = encrypt_message(K, message)
    print(f'Зашифровал сообщение {message}: {encrypted_message}')

    user.send(str(encrypted_message).encode('utf-8'))

    data = user.recv(1024)
    print(decrypt_message(K, data.decode('utf-8'))[2:-1])

