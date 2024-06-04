# Autor: Aziel de Fontes Melo
# Data: 05/03/2024

import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.dropdown import DropDown


pi = 3.14159265359

# Tabela para filtros de 2ª ordem a[0] filtros butterworth, a[1] filtros chebyshev
a = [1.414214, 2.372356]
b = [1, 3.3114037]


# # Códico da defasadora
#
# f_defasada = float(input("frequência a ser defasada \n"))
# fi_def = float(input("Defasamento desejado \n"))
#
# C_defasadora = 10*10**-9
#
# aux1 = 2*math.tan((fi_def*pi/180)/2)
# a_defasadora = (-1-(1+aux1**2)**(1/2))/aux1
#
# print(a_defasadora)
#
# R1_defasadora = 1/(2*a_defasadora*2*pi*f_defasada*C_defasadora)
# R2_defasadora = 4*R1_defasadora
# R3_defasadora = 8*R1_defasadora
# R4_defasadora = R3_defasadora
#
# print("Valores para a defasadora:")
# print("C = " + str(C_defasadora*10**9) + "nF")
# print("R1 = " + str(R1_defasadora) + "ohm")
# print("R2 = " + str(R2_defasadora) + "ohm")
# print("R3 = " + str(R3_defasadora) + "ohm")
# print("R4 = " + str(R4_defasadora) + "ohm")
# # fim do código da defasadora


kv = Builder.load_file("calculoDeParametros.kv")


class TipoDropDown(DropDown):
    pass

class FiltroScreen(Screen):

    def retorna_inteiro(self, str_obj):  # Pega o valor de uma label, string, e retorna um inteiro
        if str_obj != '':
            return float(str_obj)
        return 0

    def calcular_parametros(self):

        tipo = 1
        fc = self.retorna_inteiro(self.ids.fc_text_input.text)
        k = self.retorna_inteiro(self.ids.k_text_input.text)

        C_2 = 10 / fc

        C_2_string = str(C_2)

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

        C_1 = 0.9 * ((a[tipo]**2)*C_2)/(4*b[tipo]*(k+1))
        R_2 = (2 * (k+1)) / ((a[tipo]*C_2 + ((a[tipo]**2)*(C_2**2)-4*b[tipo]*C_1*C_2*(k+1))**(1/2))*2*pi*fc)
        R_1 = R_2 / k
        R_3 = 1 / (b[tipo]*C_1*C_2*((2*pi*fc)**2)*R_2)

        if self.retorna_inteiro(self.ids.fator_multiplicador.text) != 0 :
            fator10 = self.retorna_inteiro(self.ids.fator_multiplicador.text)
        else:
            fator10 = 1

        self.ids.C1_label.text = str(round(C_1*10**9/fator10, 3)) + " nF"
        self.ids.C2_label.text = str(round(C_2*10**9/fator10, 3)) + " nF"
        self.ids.R1_label.text = str(round(R_1*fator10, 2)) + " ohm"
        self.ids.R2_label.text = str(round(R_2*fator10, 2)) + " ohm"
        self.ids.R3_label.text = str(round(R_3*fator10, 2)) + " ohm"

    def __init__(self, **kwargs):
        super(FiltroScreen, self).__init__(**kwargs)
        tipo_drop_down = TipoDropDown()
        self.ids.tipoBotao.bind(on_release=tipo_drop_down.open)
        tipo_drop_down.bind(on_select=lambda instance, x: setattr(self.ids.tipoBotao, 'text', x))
        pass


sm = ScreenManager()
sm.add_widget(FiltroScreen(name="Filtro"))


class FiltroApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    FiltroApp().run()
