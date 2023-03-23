from kivy.app import App
from kivy.animation import Animation
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

from kivy.config import Config
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '640')
Config.set('graphics', 'height', '480')

class anApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        btn1 = Button(text='Hello')
        btn2 = Button(text='World')
        layout.add_widget(btn1)
        layout.add_widget(btn2)

        return layout


if __name__ == '__main__':
    anApp().run()