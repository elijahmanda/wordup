from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout


Builder.load_string('''
#:import gch kivy.utils.get_color_from_hex
<WordItem>
    orientation: 'vertical'
    author_name : ''
    post : ''
    
    MDCard:
        id : main_card
        size_hint_y: None
        height : int(root.height*.55)
        orientation : 'vertical'
        radius : 14
        elevation : 8
        md_bg_color : gch('#f0ff38')
        MDBoxLayout:
            id : caption_box
            size_hint_y: None
            height : int(main_card.height*.05)
            MDFloatLayout:
                size_hint: None, None
                size : caption_box.size
                MDLabel:
                    text: 'PositiveVibes@WordUp'
                    pos_hint : {'center_x': .8, 'center_y': .5}
                    font_style : 'Caption'
                    adaptive_height : True                    
        MDBoxLayout:
            orientation : 'vertical'
            size_hint_y : None
            height: int(main_card.height*.60)
            MDCard:
                id : content_card
                size_hint_y : None
                height: int(main_card.height*.60)
                radius: 14
                elevation : 8
                padding : '5dp'
                MDBoxLayout:
                    id : content_box
                    size_hint: None, None
                    height : int(main_card.height*.60)
                    height: content_card.height-15
                    width: content_card.width-15
                    size_hint: None, None
                    padding : '2dp'
                    MDLabel:
                        text: root.post
                        pos_hint : {'center_x': .5, 'center_y': .5}
                        text_size : content_box.width,None
                        size : self.texture_size
        MDBoxLayout:
            id : con_box
            size_hint_y: None
            height : int(main_card.height*.15)
            orientation : 'vertical'
            MDFloatLayout:
                size_hint: None, None
                size : con_box.size
                MDLabel:
                    text: root.author_name
                    adaptive_width: True
                    pos_hint : {'center_x': .75, 'center_y': .5}
                    font_style : 'Caption'
                    font_name : 'Roboto-Italic.ttf'
                    text_size : con_box.width ,None
                    size : self.texture_size
                MDIconButton:
                    icon: 'information-outline'
                    user_font_size: '15sp'
                    pos_hint : {'center_x': .65, 'center_y': .5}
        MDBoxLayout:
            id : btn_like_box
            size_hint_y: None
            height : int(main_card.height*.20)
            FloatLayout:
                size_hint: None, None
                size : btn_like_box.size
                pos: btn_like_box.pos
                MDIconButton:
                    icon: 'heart-outline'
                    user_font_size: '30sp'
                    pos_hint : {'center_x': .15, 'center_y': .40}
                MDIconButton:
                    icon: 'thumb-down-outline'
                    user_font_size: '30sp'
                    pos_hint : {'center_x': .35, 'center_y': .40}
                MDIconButton:
                    icon: 'share-outline'
                    user_font_size: '30sp'
                    pos_hint : {'center_x': .55, 'center_y': .40}
            
        
'''
)


class WordItem(MDBoxLayout):
    pass