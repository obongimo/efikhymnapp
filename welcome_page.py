from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from navigation_screen_manager import NavigationScreenManager


Builder.load_file("welcome_page.kv")


class MainWidget(FloatLayout):
    pass
