import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # SOCK_STREAM = tcp
sock.bind(('127.0.0.1',8888))
sock.listen(5) # сколько клиентов могут быть подключены в 1 момент
sock.setblocking(False) # сокет не будет блокироваться при ожидании клиентов
# sock.settimeout(5) # аналог блокировки, но на время. Через 5 сек сервер пойдет дальше по программе.
# если поставить 0 -> аналог без блокировки, None -> аналог блокировки 

while True:
    try:
        client, addr = sock.accept() # sock.accept() ждет подключений в стеке и при подключении клиента к серверу 
                                     # возвр. кортеж из сокета нашего клиента( sock - серверный сокет, который слушает и ждет
                                     # а это клиент-сокет, который подключается ) и его адресс + порт
    except socket.error: # так как стоит не блок режим, нужно ловить отсутствие клиентов
        print("no clients")
    except KeyboardInterrupt: # ctrl + C( выход )
        sock.close()
        break
    else:
        sock.setblocking(True) # клиент будет блокироваться( ибо ждем сообщение )
        result = client.recv(1024) # после подключения ждем сообщение
        client.close()
        print('Message', result.decode('utf-8'))