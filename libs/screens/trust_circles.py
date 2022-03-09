from kivymd.uix.screen import MDScreen
from kivy.utils import get_color_from_hex as gch
from kivymd.toast import toast
from plyer import email


class TrustCirclesPage(MDScreen):
    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.name = 'trust'
        btm_bar = self.ids['btm_nav']
        icon = btm_bar.ids['human_icon']
        icon.icon_color = gch('#daee7c')

    def add_friend(self, email, subject,help_text):
        recipient = email
        subject = subject
        text = help_text
        create_chooser = False
        email.send(recipient=recipient, subject=subject, text=text,
                   create_chooser=create_chooser)
