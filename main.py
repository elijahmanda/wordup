from logging import root
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.label import MDLabel


root = Builder.load_file("main.kv")

class HomeScreen(MDScreen) :
    pass

class WordUpApp(MDApp) :

    def build(self):
        self.theme_cls.primary_palette = "Teal"
        self.sm = ScreenManager()
        self.sm.add_widget(HomeScreen(name="home"))
        return self.sm



WordUpApp().run()