from libs.fireDB.database import collect_email, collect_password
from libs.fireDB.database import create_user, send_verification_email, verify_user, push_details, make_user_name
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from time import sleep
import string
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.properties import BooleanProperty
import json
Window.softinput_mode = "below_target"

verified = False
verify_event = None


class VerifyPage(MDScreen):
    img = StringProperty
    verify_event = BooleanProperty

    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.name = 'signup_verify'

    def first(self):
        self.img = 'assets/emoo.jpg'
        return self.img

    def second(self):
        self.img = 'assets/emoc.jpg'
        return self.img

    def third(self):
        self.img = 'assets/peek.jpg'
        return self.img

    def fourth(self):
        self.img = 'assets/emoo.jpg'
        return self.img

    def interval_verify(self, user):
        print("The user to verify...:", user)
        verified = verify_user(user)
        print("INTERVAL VERIFY CALLED", verified)
        if verified == True:
            verify_event.cancel()
            push_details()
            self.parent.current = "home"

    def verify_anim(self, email, password, password_confirm, verifybtn, image, label, label1):
        user = ''
        email_ = email.text
        password_ = password.text
        password_confirm_ = password_confirm.text
        if email.text == "":
            self.ids["email"].error = True
        elif password.text == "":
            self.ids["password"].error = True
        elif password_confirm.text == "":
            self.ids["password_confirm"].error = True
        elif password_ != password_confirm_:
            self.ids["password_confirm"].error = True

        else:
            try:
                make_user_name()
                user = create_user(str(email_), str(password_))
                collect_email(email_)
                collect_password(password_)
                self.img = 'assets/emoo.jpg'
                image.source = self.img

                anim = Animation(opacity=0, duration=0.5)
                anim.start(email)
                anim.start(password)
                anim = Animation(opacity=0, duration=0.5)
                anim.start(password_confirm)
                anim2 = Animation(opacity=0, duration=0.5)
                anim2.start(verifybtn)
                anim3 = Animation(
                    pos_hint={'center_x': .5, 'center_y': .05}, size_hint=(.3, .3), duration=1.5)
                anim3 += Animation(pos_hint={'center_x': .5,
                                   'center_y': .86}, size_hint=(.4, .4), duration=1.5)
                anim3.start(image)
                anim3 = Animation(
                    pos_hint={'center_x': .5, 'center_y': .64}, duration=3)
                anim3.start(label)
                anim4 = Animation(
                    pos_hint={'center_x': .5, 'center_y': .55}, duration=3)
                anim4.start(label1)
            except Exception as e:
                error = json.loads(e.args[1])['error']['message']
                self.ids["server_response_text"].text = str(error)

            try:
                email_sent = send_verification_email(user)
                if email_sent:
                    self.ids["server_response_text"].text = "We've sent you an email. Please verify."
                    global verify_event
                    verify_event = Clock.schedule_interval(
                        lambda dt: self.interval_verify(user), 2.5)
                    verifybtn.disabled = True
                    verifybtn.text = "Waiting..."
                    self.ids["spinner"].active = True
                    label.text = "We are creating your account..."
                    label1.text = ""
            except Exception as e:
                pass
