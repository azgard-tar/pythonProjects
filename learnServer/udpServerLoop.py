import socket

#Для доп. изучения: https://lecturesnet.readthedocs.io/net/low-level/ipc/socket/intro.html

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM )
# socket.AF_INET - используем IP протокол версии 4( 4 части ip, 0-255 ). 
# Можно так же AF_INET6 - версия 6( это в 16-ричной системе )
# socket.SOCK_DGRAM - датаграммы - негарантировання доставка( upd )
# третьим параметров можно указать протокол ( socket.IPPROTO.UPD )
sock.bind(('127.0.0.1',8888)) # резервируем адресс на компьютере. Если свободен - ошибок не будет

while True:
    try:
        result = sock.recv(1024) # пытаемся принять сообщение из сети в размере 1024 байта
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print( 'Message: ', result.decode('utf-8') )