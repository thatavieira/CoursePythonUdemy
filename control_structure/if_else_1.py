#uma função que vai converter a nota em conceito,
#retorne o conceito associado a nota.
#nota float e conceito string.
#para notas maiores que 10 e menores que 0 sera impresso "nota invalida".

#definicacao de funcao com parametro informado
#conversao de string para float
def nota_conceito(valor):
    nota = float(valor)

#comparacoes para retornar informacoes sobre notas
    if nota > 10:
        return "Nota Invalida"
    elif nota >= 9.1:
        return "A"
    elif nota >= 8.1:
        return "A-"
    elif nota >= 7.1:
        return 'B'
    elif nota >= 6.1:
        return 'B-'
    elif nota >= 5.1:
        return 'C'
    elif nota >= 4.1:
        return 'C-'
    elif nota >= 3.1:
        return 'D'
    elif nota >= 2.1:
        return 'D-'
    elif nota >= 1.1:
        return 'E'
    elif nota >= 0:
        return 'E-'
    else:
        return 'Nota Invalida'

#chamar funcao
#atencao para o input onde fica o armazenamento da nota para a validacao do if/else.
if __name__ == '__main__':
    valor_informado = input('Nota do aluno: ')
    conceito = nota_conceito(valor_informado)
    print(conceito)

