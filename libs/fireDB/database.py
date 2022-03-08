import random
import json
import re
import pyrebase
from kivy.storage.jsonstore import JsonStore
from datetime import datetime
firebaseConfig = {
    "apiKey": "AIzaSyDoZltxO33Yay0Ce4PvxO0Vg8NwjAsj01Q",

    "databaseURL": "https://wordup-yourvoice-default-rtdb.firebaseio.com/",

    "authDomain": "wordup-yourvoice.firebaseapp.com",

    "projectId": "wordup-yourvoice",

    "storageBucket": "wordup-yourvoice.appspot.com",

    "messagingSenderId": "890026830414",

    "appId": ":890026830414:web:188032f7cb0e14a90f311f",

    "measurementId": "G-2PPQV1B3GW"
}

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
storage = firebase.storage()
auth = firebase.auth()
store = JsonStore('CREDENTIALS.json')


def make_user_name():
    username = store.get('NAMES')['username']
    fname = store.get('NAMES')['fname']
    sname = store.get('NAMES')['sname']
    if username == "null":
        rep = [random.randint(0, 10) for x in range(2)]
        rep = str(rep[0])+str(rep[1])
        username = fname+str(rep)+sname[:1]
        store.put("NAMES", username=username)


def collect_fname_sname_username(fname, sname, username="null"):
    store.put('NAMES', fname=fname, sname=sname, username=username)


def collect_dob(DOB):
    store.put('DOB', dob=DOB)


def collect_email(email):
    store.put('EMAIL', email=email)


def collect_password(password):
    store.put('PASSWORD', password=password)


def read_password():
    password = store.get('PASSWORD')['password']
    return password


def read_email():
    email = store.get('EMAIL')['email']
    return email


def read_dob():
    dob = store.get('DOB')['dob']
    return dob


def read_username():
    username = store.get('NAMES')['username']
    return username


def read_fname():
    fname = store.get('NAMES')['fname']
    return fname


def read_sname():
    sname = store.get('NAMES')['sname']
    return sname


def collect_wordups():
    wordups = db.child("USERS")


def post_data(text):
    date = datetime.now()
    posted_on = date.date()
    author_name=read_username()
    post = text
    data = {"wordup": post,"author_name": author_name, "posted_on": str(posted_on)}
    db.child("WORDUP").child("posts").push(data)

def get_email_details(email):
    try:
        email = db.child("USERS").order_by_child("email").equal_to(email).get()
        return email
    except:
        pass
def get_posts():
    posts = db.child("WORDUP").order_by_child("posts").limit_to_last(7).get()
    return posts


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
        pass


def send_verification_email(user):
    try:
        auth.send_email_verification(user['idToken'])
        return True
    except Exception as e:
        return False


def push_details():
    db.child("USERS").child(read_username()).set({"email": read_email(
    ), "fname": read_fname(), "sname": read_sname(), "dob": read_dob()})


def verify_user(user):
    try:
        u = auth.get_account_info(user["idToken"])
        verified = u["users"][0]["emailVerified"]
        return verified
    except Exception as e:
        return False
