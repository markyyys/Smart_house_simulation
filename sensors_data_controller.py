
import sensors_data_collector as sc

from datetime import datetime as dt
import json
from firebase_init import *


ref = db.reference("/")
sdb = firestore.client()
sensors_num = 3
while True:
    if ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("sensorsCommand").get() != 0:
        ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("sensorsCommand").set(0)
        for i in range(sensors_num):
            data = json.loads(sc.get_data(7070, i, 'Kitchen'))
            ref.child("users").child("drvFki5nFqYh8rAKQdULYA9MAXf2").update(data)
            sref = sdb.collection('data_story').document('sen' + str(i) + "_" + str(dt.now().hour) + ":" + str(dt.now().minute) + "_" + str(dt.now().day) + "." + str(dt.now().month))
            sref.set(data)
