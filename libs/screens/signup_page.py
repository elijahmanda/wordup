from datetime import datetime
from kivymd.toast import toast
from libs.fireDB.database import collect_dob, collect_fname_sname_username, read_dob
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.screen import MDScreen
from time import time
from kivy.animation import Animation
from kivy.properties import StringProperty
from kivy.core.window import Window
import string
from kivy.utils import get_color_from_hex
Window.softinput_mode = "below_target"


class SignUp1(MDScreen):
    img = StringProperty

    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.name = 'signup_home'
        self.signup = False

    def on_save(self, instance, value, date_range):
        self.ids["datelabel"].text = str(value)
        collect_dob(str(value))

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker(min_year=2003,
                                   max_year=2011,
                                   primary_color=get_color_from_hex("#72225b"),
                                   accent_color=get_color_from_hex("#5d1a4a"),
                                   selector_color=get_color_from_hex(
                                       "#e93f39"),
                                   text_toolbar_color=get_color_from_hex(
                                       "#cccccc"),
                                   text_color=("#ffffff"),
                                   text_current_color=get_color_from_hex("#e93f39"),
                                   text_button_color=(1, 1, 1, .9),)
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()

    def signup_anim(self, fname, sname, username, dateicon, datelabel, login, image, label, label1):
        fname_ = fname.text
        sname_ = sname.text
        image = image
        username_ = username.text
        invalidChars = set(string.punctuation)
        if any(char in invalidChars for char in fname_):
            self.ids["fname"].error = True

        elif True in [char.isdigit() for char in fname_]:
            self.ids["fname"].error = True

        elif fname_ is None or sname_ is None:
            self.ids["sname"].error = True

        elif any(char in invalidChars for char in sname_):
            self.ids["sname"].error = True

        elif True in [char.isdigit() for char in sname_]:
            self.ids["sname"].error = True

        elif fname_ == "":
            self.ids["fname"].error = True

        elif sname_ == "":
            self.ids["sname"].error = True

        elif read_dob() == "null":
            toast("Enter your date of birth")

        else:
            collect_fname_sname_username(fname_, sname_, username_)
            self.parent.current = "signup_verify"
