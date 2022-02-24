from kivymd.uix.screen import MDScreen
from kivy.utils import get_color_from_hex as gch
class SupportPage(MDScreen):
    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.name='support'
        btm_bar = self.ids['btm_nav']
        icon = btm_bar.ids['info_icon']
        icon.icon_color = gch('ff7d1a')