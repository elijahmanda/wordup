

from kivy.animation import Animation
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
import json
Window.softinput_mode = "below_target"
import string
from time import sleep

from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
from libs.fireDB.database import create_user, send_verification_email


class VerifyPage(MDScreen):
    img = StringProperty
    verified = BooleanProperty(defaultvalue=False)
    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.name='signup_verify'
    
    def first(self):
        self.img = 'assets/emoo.jpg'
        return self.img
    
    def verify(self, user):
        self.verified = UserHandler.verify_user(user)
        return self.verified
    def second(self):
        self.img = 'assets/emoc.jpg'
        return self.img
    def third(self):
        self.img='assets/peek.jpg'
        return self.img
    def fourth(self):
        self.img='assets/emoo.jpg'
        return self.img
    
    def verify_anim(self,email, password,password_confirm,verifybtn,image,label,label1):
        email_ = email.text
        password_ = password.text
        password_confirm_ = password_confirm.text
        if email.text== "":
            print("Enter an email")
        elif password.text=="":
            print("Enter a password")
        elif password_confirm.text=="":
            print("Confirm password")
        elif password_!=password_confirm_:
            print("password must much")
        
        else:
            try:
                user = create_user(str(email_), str(password_))
                print(user)
                self.img='assets/emoo.jpg'
                image.source= self.img
                
                anim= Animation(opacity=0,duration=0.5)
                anim.start(email)
                anim0= Animation(opacity=0,duration=0.5)
                anim.start(password)
                anim= Animation(opacity=0,duration=0.5)
                anim.start(password_confirm)
                anim2= Animation(opacity=0,duration=0.5)
                anim2.start(verifybtn)
                anim3= Animation(pos_hint={'center_x': .5, 'center_y': .05}, size_hint=(.3,.3),duration=1.5)
                anim3+=Animation(pos_hint={'center_x': .5, 'center_y': .86}, size_hint=(.4,.4),duration=1.5)
                anim3.start(image)
                anim3= Animation(pos_hint={'center_x': .5, 'center_y': .64},duration=3)
                anim3.start(label)
                anim4= Animation(pos_hint={'center_x': .5, 'center_y': .55},duration=3)
                anim4.start(label1)
                self.send_email_verification(user)
            except Exception as e:
                print("We found: ", json.loads(e.args[1])['error']['message'])

          
