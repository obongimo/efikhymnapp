from kivy.app import App
from navigation_screen_manager import NavigationScreenManager


class EfikHymn(App):
    def build(self):
        return NavigationScreenManager()


EfikHymn().run()
