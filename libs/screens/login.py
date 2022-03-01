from libs.fireDB.database import sign_in_user
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from time import sleep
import string
from kivy.core.window import Window
from kivy.properties import StringProperty
import json
Window.softinput_mode = "below_target"

sidned_in = False


class LoginPage(MDScreen):
    img = StringProperty

    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.name = 'login'

    def login(self, email, password, image, label):
        email_ = email.text
        password_ = password.text
        if email_ == "":
            print("Enter an email")
        elif password_ == "":
            print("Enter a password")
        else:
            try:
                signed_in = sign_in_user(email, password)
                if sidned_in:
                    print("SIGN IN SUCCESS", sign_in_user)
                    self.parent.current = "home"
                    print("LOGGED IN SUCCESSFUL")
            except Exception as e:
                error = json.loads(e.args[1])['error']['message']
                label.text = str(error)

    def first(self):
        self.img = 'assets/emoo.jpg'
        return self.img

    def second(self):
        self.img = 'assets/peek.jpg'
        return self.img
