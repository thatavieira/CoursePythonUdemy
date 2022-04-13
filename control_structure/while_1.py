#while True:
#    print('vai demorar muitooo')


#randint: gerar um valor aleatorio inteiro

from random import randint

numero_informado = -1
numero_secreto = randint(0, 9)

while numero_informado != numero_secreto:
    numero_informado = int(input('informe o numero: '))

print('numero_secreto {} foi encontrado!' . format(numero_secreto))