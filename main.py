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
from kivy.uix.image import Image

# if platform == "android":
#from android.permissions import request_permissions, Permission
#request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE,Permission.INTERNET])


Window.size = [300, 600]


class WordUpApp(MDApp):
    def build(self):
        self.icon="assets/logo.jpeg"
        self.splash_screen_image = Image(source='assets/logo.jpeg', size=(0, 0))
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "500"
        self.load_all_kv_files()
        self.sm = ScreenManager(transition=SwapTransition())
        self.sm.add_widget(LoginPage())
        self.sm.add_widget(SignUp1())
        self.sm.add_widget(VerifyPage())
        self.sm.add_widget(HomePage())
        self.sm.add_widget(SupportPage())
        self.sm.add_widget(TrustCirclesPage())
        self.sm.add_widget(SettingsPage())
        self.bind(on_start=self.post_build_init)

        return self.sm

    def load_all_kv_files(self):
        Builder.load_file('libs/screens/home_page.kv')
        Builder.load_file('libs/components/bottom_nav.kv')
        Builder.load_file('libs/screens/support_page.kv')
        Builder.load_file('libs/screens/trust_circles.kv')
        Builder.load_file('libs/screens/settings_page.kv')
        Builder.load_file('libs/screens/signup_page.kv')
        Builder.load_file('libs/screens/verify_page.kv')
        Builder.load_file('libs/screens/login.kv')

    def on_start(self):
        return super().on_start()

    def on_pause(self):
        return super().on_pause()

    def on_resume(self):
        return super().on_resume()

    def on_stop(self):
        return super().on_stop()

    def post_build_init(self, *args):
        if platform == 'android':
            import android
            android.map_key(android.KEYCODE_BACK, 1001)
        win = Window
        win.bind(on_keyboard=self.my_key_handler)

    def my_key_handler(self, window, keycode1, keycode2, text, modifiers):
        if keycode1 in [27, 1001]:
            self.sm.current="home"
            return True
        return False


if __name__ == '__main__':
    WordUpApp().run()
