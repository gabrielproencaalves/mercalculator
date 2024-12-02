from kivy.app import App
from kivy.uix.widget import Widget

class Mercalculator(Widget):
    pass

class MercalculatorApp(App):
    def build(self):
        return Mercalculator()

if __name__ == '__main__':
    MercalculatorApp().run()
