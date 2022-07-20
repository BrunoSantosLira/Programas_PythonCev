from time import sleep
resposta=0
n1= int( input ('Digite um número: '))
n2= int( input ('Digite outro número:'))
while resposta != 5:
    print('\033[32m[ 1 ] SOMAR \033[m')
    print('\033[34m[ 2 ] MULTIPLICAR \033[m')
    print('\033[35m[ 3 ] MAIOR \033[m')
    print('\033[33m[ 4 ] NOVOS NÚMEROS \033[m ')
    print('\033[31m[ 5 ] SAIR... \033[m')
    resposta= int( input('Digite sua opção:'))
    print('-=-' * 12)
    if resposta == 1:
        print(f'A soma entre {n1} e {n2} resulta em {n1+n2}')
    elif resposta == 2:
        print(f'A multiplicação entre {n1} e {n2} resulta em {n1*n2}')
    elif resposta == 3:
        if n1 > n2:
            print(f'Entre {n1} e {n2}, {n1} é maior ')
        elif n2 > n1:
            print(f'Entre {n1} e {n2}, {n2} é maior ')
        else:
            print('Os valores são iguais')
    elif resposta == 4:
        n1= int(input('Digite novamente o primeiro valor: '))
        n2= int(input('Digite novamente o segundo valor: '))
    elif resposta == 5:
        sleep(0.5)
        print('Saindo...')
    else:
        print('OPÇÃO INVÁLIDA! TENTE NOVAMENTE!')