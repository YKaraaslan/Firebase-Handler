import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import json

cred = credentials.Certificate(".\service_key.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

collections = [
   {
       "document": False,
       "message": "Sample Message.",
       "new_date": False,
       "photo": False,
       "read": True,
       "receiverID": 5,
       "senderID": 1,
       "time_read": "27/10/2020 21:04:55",
       "time_sent": "27/10/2020 21:04:52",
       "time_server": firestore.SERVER_TIMESTAMP
   }
]

lists = ["5", "1"]
counter = 0

for i in collections:
    j=0
    while counter < len(lists):  
        ref = db.collection(u'Users').document(lists[counter]).collection(u'MessageRooms').document(u'rrWwboodk1H29vUpmUBy').collection('Messages').add({
                u'document': bool(i["document"]),
                u'message': i["message"],
                u'new_date': bool(i["new_date"]),
                u'photo': bool(i["photo"]),
                u'read': bool(i["read"]),
                u'receiverID': int(i["receiverID"]),
                u'senderID': int(i["senderID"]),
                u'time_read': i["time_read"],
                u'time_sent': i["time_sent"],
                u'time_server': i["time_server"]
                })
        counter += 1
        print(counter)

