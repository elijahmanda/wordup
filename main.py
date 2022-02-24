from logging import root
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel
from kivymd.theming import ThemeManager


root = Builder.load_file("main.kv")

class HomeScreen(MDScreen) :
    pass

class SupportScreen(MDScreen) :
    pass
class WordUpApp(MDApp) :

    def build(self):
        self.theme_cls  = ThemeManager()
        self.theme_cls.primary_palette = "Red"
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name="home"))
        self.sm.add_widget(SupportScreen(name="support"))
        return self.sm
    
    def switch_screen(self, name_, direction):
        self.sm.current = name_
        self.sm.transition.direction = direction
        self.sm.transition.duration = .2
        return self.sm
            



WordUpApp().run()