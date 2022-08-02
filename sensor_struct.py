import json
from datetime import datetime as dt
import random
import socket



class Sensor:
    def __init__(self, id, location):
        self.statuses = ['Working', 'Broken']
        self.id = id
        self.structure = {
            str(id) + 'Sen_' + 'id': id,
            str(id) + 'Sen_' + 'type': 'Счетчик',
            str(id) + 'Sen_' + 'location': location,
            str(id) + 'Sen_' + 'value': str(None),
            str(id) + 'Sen_' + 'status': str(None),
            str(id) + 'Sen_' + 'dateH': dt.now().hour,
            str(id) + 'Sen_' + 'dateM': dt.now().minute,
            str(id) + 'Sen_' + 'date': str(dt.now().day) + "." + str(dt.now().month)}

        self.user = self.structure.keys()
        print(self.structure)

    def set_value(self, value):
        self.structure[str(self.id) + 'Sen_' + 'value'] = value

    def set_status(self, status):
        self.structure[str(self.id) + 'Sen_' + 'status'] = self.statuses[status]

    def get_updated_data(self):
        self.structure[str(self.id) + 'Sen_' + 'dateH'] = dt.now().hour
        self.structure[str(self.id) + 'Sen_' + 'dateM'] = dt.now().minute
        self.structure[str(self.id) + 'Sen_' + 'date'] = str(dt.now().day) + "." + str(dt.now().month)
        print(self.structure)
        return json.dumps(self.structure)
