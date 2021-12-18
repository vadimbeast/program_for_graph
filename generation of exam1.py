import sympy
import math
from sympy.plotting import plot
from sympy import *
from sympy.plotting import plot3d


kol_plosk = input ('Введите количество плоскостей для вашего графика ("2" или "3"):')
kol_plosk1 = int(kol_plosk)

virazh_func = input ('Введите выражение функции после знака "=":')

diap_min = input ('Введите наименьшее значение диапозона графика:')
diap_min1 = float(diap_min)

diap_max = input ('Введите наибольшее значение диапозона графика:')
diap_max1 = float(diap_max)

def for_plosk(kol_plosk1):
    if kol_plosk1 == 3:
        x, y = symbols('x y') #для построения графика в 3х плоскостях
        plot3d(virazh_func, (x, diap_min1, diap_max1), (y, diap_min1, diap_max1))
    
    if kol_plosk1 == 2:
        x = symbols('x') #для построения графика в 2х плоскостях
        plot(virazh_func, (x, diap_min1, diap_max1), line_color='red')

for_plosk(kol_plosk1)