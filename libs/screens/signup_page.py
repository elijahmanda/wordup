from time import time
from kivy.animation import Animation
from kivy.properties import StringProperty
from kivy.core.window import Window
Window.softinput_mode = "below_target"
from kivymd.uix.screen import MDScreen
from kivymd.uix.pickers import MDDatePicker
from time import sleep
import string


class SignUp1(MDScreen):
    img = StringProperty
    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.name='signup_home'
        self.signup=False
    

    def on_save(self, instance, value, date_range):
        print(instance, value, date_range)
        self.ids["datelabel"].text=str(value)

    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''

    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
    
    
    def signup_anim(self,fname, sname,username,dateicon,datelabel ,login, image, label, label1):
        sleep(.2)
        fname_ = fname.text
        sname_ = sname.text
        image = image
        username_ = username.text
        label_ = label.text
        label1_  = label1.text
        invalidChars = set(string.punctuation)
        if any(char in invalidChars for char in fname_):
            self.ids["fname"].error= True

        elif True in [char.isdigit() for char in fname_]:
            self.ids["fname"].error=True

        elif fname_ is None or sname_ is None:
            self.ids["sname"].error= True

        elif any(char in invalidChars for char in sname_):
            self.ids["sname"].error=True

        elif True in [char.isdigit() for char in sname_]:
            self.ids["sname"].error= True

        elif fname_== "":
            self.ids["fname"].error= True

        elif sname_== "":
            self.ids["sname"].error= True
            
        else:
            self.parent.current="signup_verify"

    
        

                
        
    