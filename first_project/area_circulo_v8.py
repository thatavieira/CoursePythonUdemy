from math import pi

def circulo(raio):
    print('area do circulo', pi * float(raio) ** 2)

if __name__ == '__main__':
    raio = input('informe o raio: ')
    circulo(raio)
    