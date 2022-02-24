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


def post_data(text):
    file = open("next_id.txt", "r+")
    id = file.read().strip()
    id = int(id)
    print(id)
    data = {f'word_up{id}': str(text)}
    try :
        db.push(data)
    except Exception as e:
        print(e)
    file1 = open("next_id.txt","w")#write mode
    file1.write(str(id + 1)+" \n")
    file1.close()
