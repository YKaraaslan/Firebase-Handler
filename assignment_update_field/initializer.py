import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

cred = credentials.Certificate(".\service_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

ref = db.collection(u'Deneme').document(u'1')

ref.update({u'bsdf': "deneme12rddr3"})
