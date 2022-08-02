import json
from datetime import datetime as dt
import random

class Vacuum:
    def __init__(self, id):
        self.statuses = ['Working', 'Ready for work', 'Broken']
        self.id = id
        self.structure = {str(self.id) + 'Vac_' + 'id': self.id,
                          str(self.id) + 'Vac_' + 'type': 'Пылесос',
                          str(self.id) + 'Vac_' + 'value': str(None),
                          str(self.id) + 'Vac_' + 'status': str(None),
                          str(self.id) + 'Vac_' + 'plannedDateH': dt.now().hour,
                          str(self.id) + 'Vac_' + 'plannedDateM': dt.now().minute,
                          str(self.id) + 'Vac_' + 'plannedDate': str(dt.now().day) + "." + str(dt.now().month)}
        print(self.structure)

    def set_rand_value(self):
        if self.structure[str(self.id) + 'Vac_' +'status'] != self.statuses[0]:
            self.structure[str(self.id) + 'Vac_' +'value'] = str(None)
        else:
            self.structure[str(self.id) + 'Vac_' +'value'] = str(random.uniform(0.0, 5.0))

    def set_rand_status(self):
        i = random.randint(1, 2)
        if i == 2:
            i = random.randint(1, 2)
        else:
            if self.structure[str(self.id) + 'Vac_' +'plannedDate'] == str(dt.now().day) + "." + str(dt.now().month) \
                    and dt.now().hour <= self.structure[str(self.id) + 'Vac_' +'plannedDateH'] <= dt.now().hour + 1 \
                    and dt.now().minute <= self.structure[str(self.id) + 'Vac_' +'plannedDateM'] <= dt.now().minute + 60:
                self.structure[str(self.id) + 'Vac_' +'status'] = self.statuses[0]
                self.structure[str(self.id) + 'Vac_' +'plannedDate'] = str(dt.now().day + 1) + "." + str(dt.now().month)
            else:
                self.structure[str(self.id) + 'Vac_' +'status'] = self.statuses[i]

    def set_planned_date(self, hours, minutes, day, month):
        self.structure[str(self.id) + 'Vac_' +'plannedDateH'] = hours
        self.structure[str(self.id) + 'Vac_' +'plannedDateM'] = minutes
        self.structure[str(self.id) + 'Vac_' +'plannedDate'] = str(day) + "." + str(month)

    def get_updated_data(self):
        self.set_rand_status()
        self.set_rand_value()

        print(self.structure)
        return json.dumps(self.structure)

