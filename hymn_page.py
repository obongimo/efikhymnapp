from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label

Builder.load_file("hymn_page.kv")


class HymnPage(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        file = open('hymns/1.txt', 'r', encoding='utf-8')
        self.text = file.read()

        print(self.text)

        file.close()


# class CustomLayout(FloatLayout):
#     pass

