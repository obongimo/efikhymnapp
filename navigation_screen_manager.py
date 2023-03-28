from kivy.clock import Clock
from kivy.properties import ObjectProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager


class NavigationScreenManager(ScreenManager):
    screen_stack = []
    progress_bar = NumericProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.switch_screen, 1/25)

    def switch_screen(self, dt, *args):
        if self.current == "welcome_page":
            self.progress_bar += dt
            if self.progress_bar >= 5:
                self.current = "menu_page"
                Clock.unschedule(self.switch_screen)

    def push(self, screen_name):
        self.screen_stack.append(self.current)
        self.transition.direction = "left"
        self.current = screen_name

    def pop(self):
        screen_name = self.screen_stack[-1]
        del self.screen_stack[-1]
        self.transition.direction = "right"
        self.current = screen_name

