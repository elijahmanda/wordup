from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.animation import Animation
from kivy.properties import StringProperty
from kivy.core.window import Window
Window.softinput_mode = "below_target"

class MyApp(MDApp):
    img = StringProperty
    
    def build(self):
        return Builder.load_file('signup.kv')
    
    
    def first(self):
        self.img = 'assets/emomc.jpg'
        return self.img
    
    def second(self):
        self.img = 'assets/emoc.jpg'
        return self.img
    def third(self):
        self.img='assets/peek.jpg'
        return self.img
    def fourth(self):
        self.img='assets/emoo.jpg'
        return self.img
    
    def login(self,widget, widget0,widget1,widget2,widget3,widget4,widget5):
        self.img='assets/emo.png'
        anim= Animation(opacity=0,duration=0.5)
        anim.start(widget)
        anim0= Animation(opacity=0,duration=0.5)
        anim.start(widget0)
        anim= Animation(opacity=0,duration=0.5)
        anim.start(widget)
        anim1= Animation(opacity=0,duration=0.5)
        anim1.start(widget1)
        anim2= Animation(opacity=0,duration=0.5)
        anim2.start(widget2)
        anim3= Animation(pos_hint={'center_x': .5, 'center_y': .05}, size_hint=(.3,.3),duration=1.5)
        anim3+=Animation(pos_hint={'center_x': .5, 'center_y': .86}, size_hint=(.4,.4),duration=1.5)
        anim3.start(widget3)
        anim3= Animation(pos_hint={'center_x': .5, 'center_y': .64},duration=3)
        anim3.start(widget4)
        anim4= Animation(pos_hint={'center_x': .5, 'center_y': .55},duration=3)
        anim4.start(widget5)
                
        
MyApp().run()     