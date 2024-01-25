import socket

HOST = 'localhost'
PORT = 9009

def getFileFromServer(filename):
    data_transferred = 0

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))
        sock.sendall(filename.encode())

        data = sock.recv(1024)
        if not data:
            print('파일[%s]: 서버에 존재하지 않거나 전송 중 오류 발생' % filename)
            return
        
        with open('download/' + filename, 'wb') as f:
            try:
                while data:
                    f.write(data)
                    data_transferred += len(data)
                    data = sock.recv(1024)
            except Exception as e:
                print(e)

    print('전송완료[%s], 전송량[%d]' % (filename, data_transferred))

filename = input('다운로드 받을 파일 이름을 입력하세요: ')
getFileFromServer(filename)
