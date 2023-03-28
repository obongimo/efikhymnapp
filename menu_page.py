from kivy.lang import Builder
from kivy.metrics import dp
from kivy.properties import ObjectProperty, NumericProperty, StringProperty
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from navigation_screen_manager import NavigationScreenManager

Builder.load_file("menu_page.kv")


class GenerateButtons(GridLayout):
    b = ObjectProperty(Button())
    btn_num = StringProperty()
    hymn = StringProperty()

    def __init__(self, **kwargs):
        super(GenerateButtons, self).__init__(**kwargs)
        self.cols = 5
        self.spacing = 10
        for i in range(0, 200):
            self.b = Button(text=str(i + 1), size_hint=(None, None), size=(dp(50), dp(50)))
            self.b.bind(on_press=self.pressed)
            self.add_widget(self.b)

    def pressed(self, instance):
        self.btn_num = instance.text

        file = open('hymns/{}.txt'.format(self.btn_num), 'r', encoding='utf-8')
        self.hymn = file.read()

        file.close()
        NavigationScreenManager.hymn_temp = self.hymn

        set_screen = self.parent.parent.parent.parent
        set_screen.push("hymn_page")



