from math import pi
import sys

def circulo(raio):
    return pi * float(raio) ** 2

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('e necessario informar o raio do circulo')
        print('sintaxe: area_circulo <raio>')
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('area do circulo', area)
