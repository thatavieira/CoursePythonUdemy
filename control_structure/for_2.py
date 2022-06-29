
#percorrendo string
palavra = 'paralelepipedo'
for letra in palavra:
    print(letra, end=",")
print('fim')

#percorrendo lista
aprovados = ['rafaela', 'pedro', 'renato', 'maria']
for nome in aprovados:
    print(nome)

for posicao, nome in enumerate(aprovados):
    print(f'{posicao + 1})', nome)

#percorrendo tupla
dias_semana = ('domingo', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado')
for dia in dias_semana:
    print(f'hoje é {dia}')

#percorrendo conjunto
for numero in {1, 2, 3, 4, 5, 6}:
    print(numero)



