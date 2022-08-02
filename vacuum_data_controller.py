import json
from datetime import datetime as dt
import random
import vacuum

from firebase_init import *

ref = db.reference("/")
sdb = firestore.client()

vc = vacuum.Vacuum(0)

ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("vacuumPlannedDateH").set(-1)
ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("vacuumPlannedDateMi").set(-1)
ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("vacuumPlannedDateD").set(-1)
ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("vacuumPlannedDateM").set(-1)

while True:
    if ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("vacuumPlannedDateH").get() != -1:
        h = ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("vacuumPlannedDateH").get()
        mi = ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("vacuumPlannedDateMi").get()
        d = ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("vacuumPlannedDateD").get()
        m = ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("vacuumPlannedDateM").get()
        vc.set_planned_date(h, mi, d, m)
        ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("vacuumCommand").set(1)
    if ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("vacuumCommand").get() != 0:
        ref.child('users').child("drvFki5nFqYh8rAKQdULYA9MAXf2").child("vacuumCommand").set(0)
        data = json.loads(vc.get_updated_data())
        ref.child("users").child("drvFki5nFqYh8rAKQdULYA9MAXf2").update(data)
        sref = sdb.collection('data_story').document('vac' + str(0) + "_" + str(dt.now().hour) + ":" + str(dt.now().minute) + "_" + str(dt.now().day) + "." + str(dt.now().month))
        sref.set(data)