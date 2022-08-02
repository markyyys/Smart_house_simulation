import json
from datetime import datetime as dt
import random
import humidifier

from firebase_init import *

ref = db.reference("/")
sdb = firestore.client()
hd = humidifier.Humidifier(0, 'Bedroom')
sensors_num = 3

ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("humidifierPlannedDateH").set(-1)
ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("humidifierPlannedDateMi").set(-1)
ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("humidifierPlannedDateD").set(-1)
ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("humidifierPlannedDateM").set(-1)

while True:
    if ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("humidifierPlannedDateH").get() != -1:
        h = ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("humidifierPlannedDateH").get()
        mi = ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("humidifierPlannedDateMi").get()
        d = ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("humidifierPlannedDateD").get()
        m = ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("humidifierPlannedDateM").get()
        hd.set_planned_date(h, mi, d, m)
        ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("humidifierCommand").set(1)
    if ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("humidifierCommand").get() != 0:
        ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("humidifierCommand").set(0)
        data = json.loads(hd.get_updated_data())
        ref.child("users").child("drvFki5nFqYh8rAKQdULYA9MAXf2").update(data)
        sref = sdb.collection('data_story').document('hum' + str(0) + "_" + str(dt.now().hour) + ":" + str(dt.now().minute) + "_" + str(dt.now().day) + "." + str(dt.now().month))
        sref.set(data)