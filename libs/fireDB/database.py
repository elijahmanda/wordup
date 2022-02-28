import pyrebase

from dotenv import load_dotenv   
load_dotenv()                   

import os 
import firebase_admin
firebaseConfig = os.environ.get('firebaseConfig')
import json
import  random
firebaseConfig = {
    "apiKey":"AIzaSyAUX3-m-dfl96aJDVQtW9bdiCTjeAN67aE",
    "databaseURL": "https://kivyfiretest-default-rtdb.firebaseio.com/",
    "authDomain": "kivyfiretest.firebaseapp.com",
    "projectId": "kivyfiretest",
    "storageBucket": "kivyfiretest.appspot.com",
    "messagingSenderId": "34048073885",
    "appId": "1:34048073885:web:af1293fd30ec3ba283f474",
    "measurementId": "G-4HKHMB0J24"}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
storage = firebase.storage()





ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','x','y','z']

def generate_custom_token():
    idToken = random.randint(100000,999999)
    idToken = auth.create_custom_token(idToken)
    return str(idToken)


class Database:

    def post_data(text):
        user_end_data = {"wordup": str(text)}
        global_end_data = {"user": "jc", "wordup": str(text)}
        try:
            db.child("ACCOUNTS").child("USERS").child("hello").child("wordups").push(user_end_data)
        except Exception as e:
            print(e)

    def retrieve_data():
        word_text = []
        try:
            data = db.child("ACCOUNTS").child("USERS").child("user_email").child("wordups").get()
            for wordup in data.each():
                word_text.append(wordup.val()["word_up"])
        except Exception as e:
            print(e)
        return word_text




auth = firebase.auth()
    
def sign_in_user(email, password):
    try:
        user=auth.sign_in_with_email_and_password(email, password)
        return True

    except Exception as e:
        return  False

def create_user(email, password):                        
    user=auth.create_user_with_email_and_password(email, password)
    return user

def send_verification_email(user):
    auth.send_email_verification(user['idToken'])
    return True
    
def verify_user(self, user):
    try:
        user = auth.get_account_info(user["idToken"])[""]
        if user:
            return True
    except Exception as e:
        return False



    
        




