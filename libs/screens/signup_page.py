from time import time
from kivy.animation import Animation
from kivy.properties import StringProperty
from kivy.core.window import Window
Window.softinput_mode = "below_target"
from kivymd.uix.screen import MDScreen
from time import sleep
import string


class SignUp1(MDScreen):
    img = StringProperty
    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.name='signup_home'
        self.signup=False
    
    
    
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
            print ("fname contains special characters")
        elif fname_ is None or sname_ is None:
            print("Enter some values")
        elif True in [char.isdigit() for char in fname_]:
            print("No numbers allowed")
        elif any(char in invalidChars for char in sname_):
            print ("sname contains special characters")
        elif True in [char.isdigit() for char in sname_]:
            print("No numbers allowed")
        else:
            print ("No special characters")
            self.img='assets/emoo.jpg'
            image.source= self.img
            label.text='Welcome '+fname_+" "+sname_
            label1.text='Almost there finish setup'
            
            anim= Animation(opacity=0,duration=0.5)
            anim.start(fname)
            anim0= Animation(opacity=0,duration=0.5)
            anim.start(sname)
            anim= Animation(opacity=0,duration=0.5)
            anim.start(datelabel)
            anim0= Animation(opacity=0,duration=0.5)
            anim.start(dateicon)
            anim= Animation(opacity=0,duration=0.5)
            anim.start(datelabel)
            anim1= Animation(opacity=0,duration=0.5)
            anim1.start(login)
            
            anim3= Animation(pos_hint={'center_x': .5, 'center_y': .05}, size_hint=(.3,.3),duration=1.5)
            anim3+=Animation(pos_hint={'center_x': .5, 'center_y': .86}, size_hint=(.4,.4),duration=1.5)
            anim3.start(image)
            anim3= Animation(pos_hint={'center_x': .5, 'center_y': .64},duration=3)
            anim3.start(label)
            anim4= Animation(pos_hint={'center_x': .5, 'center_y': .55},duration=3)
            anim4.start(label1)
            self.signup=False
            self.parent.current="signup_verify"

    
        

                
        
    