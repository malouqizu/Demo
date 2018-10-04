import socket
if __name__=="__main__":
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(("127.0.0.1",8001))
    while True:
        print(sock.recv(1024))
        sendMsg = input("Please input:")
        sock.sendall(bytes(sendMsg,encoding="utf8"))
    sock.close()
