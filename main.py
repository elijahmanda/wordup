__version__="1.0"
from kivy.utils import platform
if platform == "android":
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE,Permission.INTERNET])
from kivymd.app import MDApp
from kivy.lang import Builder
from libs.screens.home_page import HomePage
from libs.screens.support_page import SupportPage
from libs.screens.trust_circles import TrustCirclesPage
from libs.screens.settings_page import SettingsPage
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
Window.size=[300, 600]

class WordUpApp(MDApp):
    def build(self):
        self.theme_cls.theme_style='Light'
        self.theme_cls.primary_palette="DeepPurple"
        self.theme_cls.primary_hue = "500"
        self.load_all_kv_files()
        global sm
        sm = ScreenManager()
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
    
        
if __name__=='__main__':
    WordUpApp().run()
        