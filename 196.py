import socket

HOST = 'localhost'
PORT = 9009

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((HOST, PORT))

    while True:
        msg = input('메시지 입력: ')
        if msg == '/quit':
            sock.sendall(msg.encode())
            break

        sock.sendall(msg.encode())
        data = sock.recv(1024)
        print('에코 서버로부터 받은 데이터 [%s]' %data.decode())
        print('에코 서버로부터 받은 데이터 [%s]' %data.decode())

print('클라이언트 종료')