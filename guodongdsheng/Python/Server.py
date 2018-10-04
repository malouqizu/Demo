import socket

if __name__=="__main__":
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.bind(("127.0.0.1",8001))
    sock.listen(5)
    sock_list = []
    print("Server is running...")
    while True:
        client,cleint_addr = sock.accept()
        print(client,"---",cleint_addr)
        client.sendall(("Welcome to Python Server!").encode("utf8"))
        buf = client.recv(1024)
        print(buf)
    sock.close()