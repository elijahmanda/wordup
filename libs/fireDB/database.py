import pyrebase

firebaseConfig = {"apiKey": "AIzaSyAUX3-m-dfl96aJDVQtW9bdiCTjeAN67aE",
    "databaseURL": "https://kivyfiretest-default-rtdb.firebaseio.com/",
    "authDomain": "kivyfiretest.firebaseapp.com",
    "projectId": "kivyfiretest",
    "storageBucket": "kivyfiretest.appspot.com",
    "messagingSenderId": "34048073885",
    "appId": "1:34048073885:web:af1293fd30ec3ba283f474",
    "measurementId": "G-4HKHMB0J24"
}
firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()
import random


def post_data(text):
    id = random.random()
    print(id)
    data = {'word_up': str(text)}
    try :
        db.push(data)
    except Exception as e:
        print(e)
    
