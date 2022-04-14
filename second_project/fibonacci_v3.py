# 0,1,1,2,3,5,8,13,21...
#while - com limite

def fibonacci(limite):
    penultimo = 0
    ultimo = 1
    print(f' {penultimo}, {ultimo}', end=',')
    while ultimo < limite:
        penultimo: int = ultimo, penultimo + ultimo
        print(ultimo, end=',')

if __name__ == '__main__':
    fibonacci(10000)
