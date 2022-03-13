from kivymd.uix.screen import MDScreen
from kivy.utils import get_color_from_hex as gch
from kivymd.toast import toast


class TrustCirclesPage(MDScreen):
    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.name = 'trust'
        btm_bar = self.ids['btm_nav']
        icon = btm_bar.ids['human_icon']
        icon.icon_color = gch('#daee7c')

    def add_friend(self, email):
        toast("Oops something went wrong")
