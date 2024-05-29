from kivymd.app import MDApp
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import MDScreen
from kivy.metrics import dp
from kivymd.uix.screenmanager import MDScreenManager

class LoginScreen(MDScreen):
    pass

class Receitas(MDScreen):
    pass

class Pudim(MDScreen):
    pass

class CupCake(MDScreen):
    pass

class PaoDeMel(MDScreen):
    pass

class Comecar(MDScreen):
    pass


class App(MDApp, App):
    def build(self):
        Window.size = (dp(300), dp(600))
        Builder.load_file(('main.kv'))
        self.theme_cls.primary_palette = 'Gray'
        telas = MDScreenManager()
        telas.add_widget(LoginScreen())
        telas.add_widget(Comecar())
        telas.add_widget(Receitas())
        telas.add_widget(Pudim())
        telas.add_widget(CupCake())
        telas.add_widget(PaoDeMel())
        return telas

App().run()