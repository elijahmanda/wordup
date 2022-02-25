from kivymd.uix.screen import MDScreen
from kivy.utils import get_color_from_hex as gch
class TrustCirclesPage(MDScreen):
    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.name='trust'
        btm_bar = self.ids['btm_nav']
        icon = btm_bar.ids['human_icon']
        icon.icon_color = gch('#daee7c')