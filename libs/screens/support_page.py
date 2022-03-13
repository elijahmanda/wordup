from kivymd.uix.screen import MDScreen

from plyer import email
from kivymd.toast import toast
from libs.fireDB.database import read_sname, read_fname, read_email


class SupportPage(MDScreen):
    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.name = 'support'
        btm_bar = self.ids['btm_nav']
        icon = btm_bar.ids['info_icon']
        icon.icon_color = gch('ff7d1a')

    def send_help(self, dest):
        toast("Email has been sent to "+dest)
        try:
            if dest == "Zicta":
                recipient = 'info@zicta.com'
            elif dest == "Police":
                recipient = 'zpwebsitesupport@zambiapolice.org.zm'
            #elif dest == "Trust Circles":
            #    recipient = 'yourfriend@gmail.com'
            elif dest == "humanrights":
                recipient="registrar-kshrc@karnataka.gov.in."
            subject = "Cyber abuse"
            text = f"I'm experiencing online abuse and I in need help, my name is {read_fname()} {read_sname() my email is {read_email()}."
            create_chooser = False
            email.send(recipient=recipient, subject=subject, text=text,
                       create_chooser=create_chooser)
            toast("Email will be sent to "+dest)
        except:
            toast("Please check your Internet connection...")
