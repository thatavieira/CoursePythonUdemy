palavras_proibidas = ('futebol', 'religiao', 'politica')
textos = [
    'joao gosta de futebol e politica',
    'a praia foi divertida'
]

for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in palavras_proibidas:
            print('texto possui pelo menos uma palavra proibida', palavra)
            found = True
            break

if not found:
    print('texto autorizado:')