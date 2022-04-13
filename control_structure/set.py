palavras_proibidas = {'futebol', 'religiao', 'politica'}
textos = [
    'joao gosta de futebol e politica',
    'a praia foi divertida'
]

for texto in textos:
    intersecao = palavras_proibidas.intersection(set(texto.lower().split()))
    if intersecao:
        print('texto possui palavras proibidas', intersecao)
    else:
        print('texto autorizado:', texto)