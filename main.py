from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

class Mercalculator(Widget):
    # Hook para o botao X
    eval_x = ObjectProperty(None)
    # Hook para o botao clear
    clear = ObjectProperty(None)
    # Hook para o label de saída
    output = ObjectProperty(None)
    # Hook para a caixa de insercao 1
    numor1 = ObjectProperty(None)
    # Hook para a caixa de insercao 2
    denor1 = ObjectProperty(None)
    # Hook para a caixa de insercao 3
    numor2 = ObjectProperty(None)

    def evaluate_x(self):
        try:
            n1 = float(self.numor1.text.replace(',', '.'))
            d1 = float(self.denor1.text.replace(',', '.'))
            n2 = float(self.numor2.text.replace(',', '.'))
            self.output.text = "%.2f" % ((n2 * d1)/n1)
        except:
            return True

    def clearall(self):
        self.output.text = "?"
        self.numor1.text = ""
        self.denor1.text = ""
        self.numor2.text = ""
        return True

    # Caso um toque ocorra em algum lugar
    def on_touch_down(self, touch):
        # Se for no botao eval_x
        if self.eval_x.collide_point(*touch.pos):
            return self.evaluate_x()
        # Se for no botao clear
        if self.clear.collide_point(*touch.pos):
            return self.clearall()
        # Senao, aja naturalmente
        super(Mercalculator, self).on_touch_down(touch)

class MercalculatorApp(App):
    def build(self):
        return Mercalculator()

if __name__ == '__main__':
    MercalculatorApp().run()
