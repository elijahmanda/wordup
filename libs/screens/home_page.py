from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.swiper import MDSwiper
from kivymd.uix.swiper import MDSwiperItem
from kivymd.uix.boxlayout import MDBoxLayout
from libs.components.card_custom import MD3Card
from kivy.utils import get_color_from_hex as gch
from libs.screens.ui_manager import ScreenManager
from kivy.clock import Clock
from libs.fireDB.database import post_data

class HomePage(MDScreen):
    def __init__(self, *kwargs):
        super().__init__(*kwargs)
        self.name='home'
        btm_bar = self.ids['btm_nav']
        icon = btm_bar.ids['home_icon']
        icon.icon_color = gch('#7ceaee')
       
    def add_card(self, text):
        post_data(text)
        self.style='elevated'       
        item=MDSwiperItem()
        card = MD3Card(
            orientation='vertical',
            radius=[14,14,0,0],
            elevation=8,
            style=self.style,
            md_bg_color=gch('#ffffff'),
            )
        box=MDBoxLayout(
            orientation='vertical',
            pos=card.pos,
            size=(card.size),
            )
        label=MDLabel(text=text, halign='center')
        box.add_widget(label)
        card.add_widget(box)
        item.add_widget(card)
        self.ids['swiper'].add_widget(item)
                
       