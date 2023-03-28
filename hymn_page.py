from kivy.lang import Builder
from kivy.properties import StringProperty, ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from navigation_screen_manager import NavigationScreenManager

Builder.load_file("hymn_page.kv")


class HymnPage(BoxLayout):
    hymn_label = ObjectProperty()
    hymn_no = ObjectProperty()
    text = StringProperty()

    def on_touch_down(self, touch):
        self.text = NavigationScreenManager.hymn_temp


class GenerateHymn(GridLayout):
    pass
