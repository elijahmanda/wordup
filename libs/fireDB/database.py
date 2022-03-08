import random
import json
import pyrebase
import sqlite3

import os
import firebase_admin
firebaseConfig = os.environ.get('firebaseConfig')
firebaseConfig = {
    "apiKey": "AIzaSyAUX3-m-dfl96aJDVQtW9bdiCTjeAN67aE",
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
try:
    conn = sqlite3.connect('USER_CRED.db')
    conn.execute('''CREATE TABLE USER_CREDENTIALS
        (              
         FIRSTNAME      TEXT,
         SECONDNAME     TEXT,
         USERNAME       TEXT,
         AGE            INT,
         DOB      INT,
         EMAIL        CHAR(50),
         UID          TEXT,
         PASSWORD           CHAR(20));''')
except Exception as e:
    pass


def collect_fname_sname_username(fname, sname, username):
    try:
        script = "INSERT INTO USER_CREDENTIALS (FIRSTNAME, SECONDNAME, USERNAME) VALUES (?, ?, ?);"
        conn.execute(script, (fname, sname, username))
        conn.commit()
    except Exception as e:
        pass


def collect_dob(DOB):
    try:
        script = "INSERT INTO USER_CREDENTIALS (DOB) VALUES (?);"
        conn.execute(script, (DOB))
        conn.commit()
    except Exception as e:
        pass

def collect_uid(UID):
    try:
        script = "INSERT INTO USER_CREDENTIALS (UID) VALUES (?);"
        conn.execute(script, (UID)
        conn.commit()
    except Exception as e:
        pass


def post_data(text):
    user_end_data = {"wordup": str(text)}
    try:
        db.child("USERS").child(user).child("wordups").set(user_end_data)
    except Exception as e:
        print(e)


def retrieve_data():
    word_text = []
    try:
        data = db.child("ACCOUNTS").child("USERS").child(userid).child("wordups").get()
        for wordup in data.each():
            word_text.append(wordup.val()["word_up"])
    except Exception as e:
        print(e)
    return word_text


auth = firebase.auth()


def sign_in_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return True
    except Exception as e:
        return False


def create_user(email, password):
    try:
        user = auth.create_user_with_email_and_password(email, password)
        return user
    except Exception as e:
        print(e)


def send_verification_email(user):
    try:
        auth.send_email_verification(user['idToken'])
        return True
    except Exception as e:
        return False


def verify_user(user):
    print("............ELIJAH PASSED HERE.........")
    try:
        u = auth.get_account_info(user["idToken"])
        verified = u["users"][0]["emailVerified"]
        print("Auth info....:", u)
        return verified
    except Exception as e:
        return False
