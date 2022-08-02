import json
import random
import socket

sock = socket.socket()
sock.bind(('', 7070))
sock.listen(1)

info = True
while True:
    conn, addr = sock.accept()
    try:
        value = str(random.uniform(0.0, 5.0))
        status = random.randint(0, 1)
        if info:
            info = False
            conn.send(json.dumps({'value': value, 'status': status}).encode('utf-8'))
        data = conn.recv(1024)
        print(data)
        if data:
            info = True
    except ConnectionResetError:
        continue

conn.close()