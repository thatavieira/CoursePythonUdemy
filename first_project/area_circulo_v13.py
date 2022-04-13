from math import pi
import sys

def help():
    print('e necessario informar o raio do circulo')
    print('sintaxe: {} <raio>'. format(sys.argv[0][2:]))

def circulo(raio):
    return pi * float(raio) ** 2

if __name__ == '__main__':
    if len(sys.argv) < 2:
        help ()
        # sys.exit(errno.EPERM)
    else:
        raio = sys.argv[1]
        area = circulo(raio)
        print('area do circulo', area)
