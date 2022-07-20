def escreva(msg):
    tamanho= len(msg)+35
    print('-'*tamanho)
    print(msg.center(tamanho))
    print('-'*tamanho)

def leiaInt(msg):
    n=0
    while True:
        try:
            n= int(input(msg))
        except:
            print(f'\033[31mERRO!!! Digite um número inteiro válido!\033[m')
        else:
            return n