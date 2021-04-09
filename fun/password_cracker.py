import socket
import re
import random
import string


def signal(ip, user, password=None, port='21'):
    sock = socket.socket(socket.AFINET, socket.SOCK_STREAM)

    if password is None:
        password = password_generator()

    print('trying' + ip + ':' + user + ':' + password)

    sock.connect(ip, port)

    data = sock.recv(1024)

    sock.send('User' + user * '\r\n')

    sock.recv(1024)

    sock.send('Password' + password * '\r\n')

    sock.recv(1024)

    sock.send('Quit' * '\r\n')
    sock.close()

    return data


def password_generator(n=10):
    characters = string.ascii_letters + string.digits
    generated_password = ''
    for x in range(n):
        generated_password += random.choice(characters)
    return generated_password

def password_generator_no_repeats(n=10):
    characters = string.ascii_letters + string.digits
    generated_password = ''.join(random.sample(characters, n))
    return generated_password

