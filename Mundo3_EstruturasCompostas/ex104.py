def leiaint(n):
    while n.isnumeric()== False:
        n= input('Digite um número')
        if n.isnumeric() == False:
            print('\033[31mERRO!!! Digite apenas um número inteiro para continuar\033[m')
    return n


n= leiaint('Digite um número')
print(f'Você acabou de digitar o número {n}')


