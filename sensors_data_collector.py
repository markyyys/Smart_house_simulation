import json
import random
import socket
import sensor_struct


def get_data(port, id, location):
    sens = sensor_struct.Sensor(id, location)
    sock = socket.socket()
    sock.connect(('localhost', port))
    sock.send(str('info').encode('utf-8'))
    while True:
        message = sock.recv(1024)
        if message:
            print(message)
            data = json.loads(message)
            sens.set_status(data['status'])
            sens.set_value(data['value'])
            sens.get_updated_data()
            break
    sock.close()
    return sens.get_updated_data()
