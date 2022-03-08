from kivy.uix.carousel import Carousel
from kivymd.toast import toast
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.swiper import MDSwiper
from kivymd.uix.swiper import MDSwiperItem
from kivymd.uix.boxlayout import MDBoxLayout
from libs.components.card_custom import MD3Card
from kivy.utils import get_color_from_hex as gch
from libs.screens.ui_manager import ScreenManager
from kivy.clock import Clock
from kivy.lang.builder import Builder
from libs.components.card import WordItem
from libs.fireDB.database import get_posts, post_data


class HomePage(MDScreen):
    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.name = 'home'
        btm_bar = self.ids['btm_nav']
        icon = btm_bar.ids['home_icon']
        icon.icon_color = gch('#7ceaee')
        

    def on_enter(self):
        self.add_content()

    def post_card(self, text):
        post_data(text)

    def add_content(self):
        data = get_posts()
        if data.each()==None:
            toast("No post yet")
        else:
            data = get_posts()
            for post_ in data.each():
                post_dict= post_.val()
                keys = post_dict.keys()
                for key in keys:
                    author_name=post_dict[key]["author_name"]
                    post=post_dict[key]["wordup"]
                    item = WordItem()
                    item.author_name = 'Written by '+author_name
                    item.post = post
                    self.ids['carousel'].add_widget(item)
        
