import firebase_admin
from firebase_admin import db
from firebase_admin import firestore
cred_obj = firebase_admin.credentials.Certificate('smarthouseapi-firebase-adminsdk-17q86-283b1a7603.json')
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL': 'https://smarthouseapi-default-rtdb.firebaseio.com/'})