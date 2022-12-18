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


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

# Генерирую a, p, g
a = random.randint(1000, 10000)
p = random.randint(1000, 10000)
g = random.randint(1000, 10000)

A = (g ** a) % p

print(client.recv(1024).decode('utf-8'))

client.send(str(A).encode('utf-8'))
client.send(str(g).encode('utf-8'))
client.send(str(p).encode('utf-8'))

# Получаю B
B = client.recv(1024).decode('utf-8')

K = (int(B)**a) % p
print('Полученное число К: ', K)

while True:

    data = client.recv(1024)
    print(f'Получил сообщение от сервера: {data.decode("utf-8")}')
    print('Расшифрованное сообщение: ', decrypt_message(K, str(data.decode('utf-8'))[2:-1]))

    print('**Введите сообщение для сервера:** ', end='')
    message = str(input().encode('utf-8'))

    encrypted_message = encrypt_message(K, message)
    print(f'Зашифровал сообщение {message}: {encrypted_message}')

    client.send(str(encrypted_message).encode('utf-8'))

