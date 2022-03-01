__version__ = "1.1.1"

from libs.screens.login import LoginPage
from kivymd.font_definitions import theme_font_styles
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, SwapTransition
from libs.screens.verify_page import VerifyPage
from libs.screens.signup_page import SignUp1
from libs.screens.settings_page import SettingsPage
from libs.screens.trust_circles import TrustCirclesPage
from libs.screens.support_page import SupportPage
from libs.screens.home_page import HomePage
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.utils import platform

# if platform == "android":
#from android.permissions import request_permissions, Permission
#request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE,Permission.INTERNET])


Window.size = [300, 600]


class WordUpApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "500"
        self.load_all_kv_files()
        global sm
        sm = ScreenManager(transition=SwapTransition())
        sm.add_widget(LoginPage())
        sm.add_widget(SignUp1())
        sm.add_widget(VerifyPage())
        sm.add_widget(HomePage())
        sm.add_widget(SupportPage())
        sm.add_widget(TrustCirclesPage())
        sm.add_widget(SettingsPage())

        return sm

    def load_all_kv_files(self):
        Builder.load_file('libs/screens/home_page.kv')
        Builder.load_file('libs/components/bottom_nav.kv')
        Builder.load_file('libs/screens/support_page.kv')
        Builder.load_file('libs/screens/trust_circles.kv')
        Builder.load_file('libs/screens/settings_page.kv')
        Builder.load_file('libs/screens/signup_page.kv')
        Builder.load_file('libs/screens/verify_page.kv')
        Builder.load_file('libs/screens/login.kv')


if __name__ == '__main__':
    WordUpApp().run()
