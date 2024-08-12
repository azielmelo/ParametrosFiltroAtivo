# Autor: Aziel de Fontes Melo
# Data: 05/03/2024

import os

os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.dropdown import DropDown
import math


pi = 3.14159265359

# Tabela para filtros de 4ª ordem filtros butterworth,
a = 0.765367
b = 1
#a = 1.847759
#b = 1
# filtros chebyshev 4ª ordem
#a = 1.275460
#b = 0.622925
#a = 0.528313
#b = 1.330031

# Códico da defasadora

f_defasada = float(input("frequência a ser defasada \n"))
fi_def = float(input("Defasamento desejado \n"))
C_defasadora = 100*10**-9
aux1 = 2*math.tan((fi_def*pi/180)/2)

if fi_def > 0:
    a_defasadora = (-1 + (1 + aux1 ** 2) ** (1 / 2)) / aux1
else:
    a_defasadora = (-1 - (1 + aux1 ** 2) ** (1 / 2)) / aux1

print(aux1)

R1_defasadora = 1/(2*a_defasadora*2*pi*f_defasada*C_defasadora)
R2_defasadora = 4*R1_defasadora
R3_defasadora = 8*R1_defasadora
R4_defasadora = R3_defasadora

print("Valores para a defasadora:")
print("C = " + str(C_defasadora*10**9) + "nF")
print("R1 = " + str(R1_defasadora) + "ohm")
print("R2 = " + str(R2_defasadora) + "ohm")
print("R3 = " + str(R3_defasadora) + "ohm")
print("R4 = " + str(R4_defasadora) + "ohm")
# fim do código da defasadora


kv = Builder.load_file("calculoDeParametros.kv")


class TipoDropDown(DropDown):
    pass

class FiltroScreen(Screen):

    def retorna_inteiro(self, str_obj):  # Pega o valor de uma label, string, e retorna um inteiro
        if str_obj != '':
            return float(str_obj)
        return 0

    def calcular_parametros(self):

        fc = self.retorna_inteiro(self.ids.fc_text_input.text)
        k = self.retorna_inteiro(self.ids.k_text_input.text)
        p = self.retorna_inteiro(self.ids.p_text_input.text)

        C_2 = 0.00001 / fc

        C_1 = p * ((a**2)*C_2)/(4*b*(k+1))
        R_2 = (2 * (k+1)) / ((a*C_2 + ((a**2)*(C_2**2)-4*b*C_1*C_2*(k+1))**(1/2))*2*pi*fc)
        R_1 = R_2 / k
        R_3 = 1 / (b*C_1*C_2*((2*pi*fc)**2)*R_2)

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


class DefasadoraScreen(Screen):
    pass


sm = ScreenManager()
sm.add_widget(FiltroScreen(name="Filtro"))
sm.add_widget(DefasadoraScreen(name="Defasadora"))


class FiltroApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    FiltroApp().run()
