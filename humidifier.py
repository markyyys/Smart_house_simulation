import json
from datetime import datetime as dt
import random

class Humidifier:
    def __init__(self, id, location):
        self.statuses = ['Working', 'Ready for work', 'Broken']
        self.id = id
        self.structure = {str(self.id) + 'Hum_' + 'id': id,
                          str(self.id) + 'Hum_' + 'type': 'Увлажнитель',
                          str(self.id) + 'Hum_' + 'location': location,
                          str(self.id) + 'Hum_' + 'status': str(None),
                          str(self.id) + 'Hum_' + 'plannedDateH': dt.now().hour,
                          str(self.id) + 'Hum_' + 'plannedDateM': dt.now().minute,
                          str(self.id) + 'Hum_' + 'plannedDate': str(dt.now().day) + "." + str(dt.now().month)}
        print(self.structure)

    def set_rand_status(self):
        i = random.randint(1, 2)
        if i == 2:
            i = random.randint(1, 2)
        else:
            if self.structure[str(self.id) + 'Hum_' + 'plannedDate'] == str(dt.now().day) + "." + str(dt.now().month) \
                    and dt.now().hour <= self.structure[str(self.id) + 'Hum_' + 'plannedDateH'] <= dt.now().hour + 1 \
                    and dt.now().minute <= self.structure[str(self.id) + 'Hum_' + 'plannedDateM'] <= dt.now().minute + 60:
                self.structure[str(self.id) + 'Hum_' + 'status'] = self.statuses[0]
                self.structure[str(self.id) + 'Hum_' + 'plannedDate'] = str(dt.now().day + 1) + "." + str(dt.now().month)
            else:
                self.structure[str(self.id) + 'Hum_' + 'status'] = self.statuses[i]

    def set_planned_date(self, hours, minutes, day, month):
        self.structure[str(self.id) + 'Hum_' + 'plannedDateH'] = hours
        self.structure[str(self.id) + 'Hum_' + 'plannedDateM'] = minutes
        self.structure[str(self.id) + 'Hum_' + 'plannedDate'] = str(day) + "." + str(month)

    def get_updated_data(self):
        self.set_rand_status()
        print(self.structure)
        return json.dumps(self.structure)
