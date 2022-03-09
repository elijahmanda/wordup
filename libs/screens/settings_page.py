from kivymd.uix.screen import MDScreen
from kivy.utils import get_color_from_hex as gch
from libs.screens.ui_manager import ScreenManager

class SettingsPage(MDScreen):
    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.name='settings'
        