from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
Screen:

    MDSpinner:
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {'center_x': .5, 'center_y': .5}
        active: True if check.active else False

    MDCheckbox:
        id: check
        size_hint: None, None
        size: dp(48), dp(48)
        pos_hint: {'center_x': .5, 'center_y': .4}
        active: True
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()