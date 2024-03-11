# Autor: Aziel de Fontes Melo
# Data: 05/03/2024

import os


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

pi = 3.14159265359

# Tabela para filtros butterworth
a = [1.414214, 1, 0.765367, 0.618034, 0.517638, 0.445042, 0.390181]
b = 1

kv = Builder.load_file("calculoDeParametros.kv")


class FiltroScreen(Screen):

    def retorna_inteiro(self, str_obj):  # Pega o valor de uma label, string, e retorna um inteiro
        if str_obj != '':
            return float(str_obj)
        return 0

    def calcular_parametros(self):

        fc = self.retorna_inteiro(self.ids.fc_text_input.text)
        k = self.retorna_inteiro(self.ids.k_text_input.text)

        C_2 = 10 / fc

        C_2_string = str(C_2)

        C_2 = 1

        for i in C_2_string:
            if i == '0':
                C_2 = C_2 * 0.1
            elif i != '.':
                if i == '1':
                    C_2 = C_2 * 1
                    break
                elif i == '2':
                    C_2 = C_2 * 2.2
                    break
                elif i == '3':
                    C_2 = C_2 * 3.3
                    break
                elif i == '4':
                    C_2 = C_2 * 4.7
                    break
                elif i == '5':
                    C_2 = C_2 * 4.7
                    break
                elif i == '6':
                    C_2 = C_2 * 5.6
                    break
                elif i == '7':
                    C_2 = C_2 * 6.8
                    break
                elif i == '8':
                    C_2 = C_2 * 10
                    break
                elif i == '9':
                    C_2 = C_2 * 10
                    break


        C_1 = 0.9 * ((a[0]**2)*C_2)/(4*b*(k+1))
        R_2 = (2 * (k+1)) / ((a[0]*C_2 + ((a[0]**2)*(C_2**2)-4*b*C_1*C_2*(k+1))**(1/2))*2*pi*fc)
        R_1 = R_2 / k
        R_3 = 1 / (b*C_1*C_2*((2*pi*fc)**2)*R_2)

        self.ids.C1_label.text = str(round(C_1*10**9/10000, 3)) + " nF"
        self.ids.C2_label.text = str(round(C_2*10**9/10000, 3)) + " nF"
        self.ids.R1_label.text = str(round(R_1*10000, 2)) + " ohm"
        self.ids.R2_label.text = str(round(R_2*10000, 2)) + " ohm"
        self.ids.R3_label.text = str(round(R_3*10000, 2)) + " ohm"

    def __init__(self, **kwargs):
        super(FiltroScreen, self).__init__(**kwargs)
        pass

class FiltroApp(App):

    def build(self):
        return FiltroScreen()

if __name__ == '__main__':
    FiltroApp().run()
