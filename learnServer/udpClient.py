import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto( input("Введите строку:").encode('utf-8') , ('127.0.0.1',8888))