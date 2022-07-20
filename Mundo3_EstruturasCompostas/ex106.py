from time import sleep
resposta=0

cores = {'sem': '\033[m]',
         'vermelho': '\033[1;41m',
         'verde': '\033[1;42m',
         'amarelo': '\033[1;43m',
         'azul': '\033[1;44m',
         'roxo': '\033[1;45m'}


def escreva(msg):
    tamanho= len(msg) +4
    print(f'~'*tamanho)
    print(f'  {msg}')
    print(f'~'*tamanho)




while True:
    print('\033[1;30;42m')
    escreva('SISTEMA DE AJUDA PYHELP')
    print('\033[m')
    sleep(1)

    resposta= str(input('Função ou Biblioteca -> '))
    if resposta.upper() == 'FIM':
        escreva('\033[35m Obrigado por usar ;/')
        break

    else:
        print('\033[0;30;46m')
        escreva(f'Acessando o manual do comando "{resposta}" ')
        print('\033[m')
        sleep(1)
        print('\033[7;30m')
        help(resposta)
        print('\033[m')
        sleep(1)




