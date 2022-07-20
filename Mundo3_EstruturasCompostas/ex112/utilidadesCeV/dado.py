def leiaDinheiro(msg):
    while True:
        entrada =  str(input(msg)).strip()
        entrada = entrada.replace(',','.')
        if entrada.isalpha() or entrada == '':
            print(f'\033[31m ERRO! "{entrada}" não é valor monetário válido\033[m')
        else:
            return float(entrada)


def leiaint(n):
    while n.isnumeric()== False:
        n= input('Digite um número')
        if n.isnumeric() == False:
            print('\033[31mERRO!!! Digite apenas um número inteiro para continuar\033[m')
    return n
