def leiaInt(msg):
    n=0
    while True:
        try:
            n= int(input(msg))
        except:
            print(f'\033[31mERRO!!! Digite um número inteiro válido!\033[m')
        else:
            return n


def leiaFloat(msg):
    n=0
    while True:
        try:
            n= str(input(msg))
            n= n.replace(',','.')
            if n.isalpha():
                print(f'\033[31mERRO!!! Digite um número decimal válido!!!\033[m')
                continue
        except KeyboardInterrupt:
            print(f'O usuário preferiu não digitar nenhum número')
            n= 0
            return n
        except:
            print(f'\033[31mERRO!!! Digite um valor decimal válido!\033[m')
        else:
            return float(n)