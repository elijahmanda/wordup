from libs.fireDB.database import collect_uid, sign_in_user
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from time import sleep
import string
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivymd.toast import toast
import json
Window.softinput_mode = "below_target"

from libs.fireDB.database collect_uid
sidned_in = False


class LoginPage(MDScreen):
    img = StringProperty()

    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.name = 'login'

    def login(self, email, password, image, label):
        email_ = email.text
        password_ = password.text
        if email_ == "":
            self.ids["label"].text = "Please enter an email"
        elif password_ == "":
            self.ids["label"].text = "Please enter a password"

        else:
            try:
                signed_in = sign_in_user(email_, password_)
                user = auth.refresh(sidned_in['refreshToken'])
                # now we have a fresh token
                collect_uid(user['idToken'])
                if signed_in:
                    self.parent.current = "home"
                    toast("LOGGED IN SUCCESSFUL")
            except Exception as e:
                error = json.loads(e.args[1])['error']['message']
                self.ids["label"].text = str(error)

    def first(self):
        self.img = 'assets/emoo.jpg'
        return self.img

    def second(self):
        self.img = 'assets/peek.jpg'
        return self.img
