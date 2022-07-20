from ex115 import funções
from time import sleep

opção = 0
cores= {
        'Sem': '\033[m',
        'Vermelho': '\033[31m',
        'Verde': '\033[32m',
        'Amarelo': '\033[33m',
        'Azul Escuro' : '\033[34m',
        'Roxo': '\033[35m',
        'Azul Claro': "\033[36m"}

while opção != 3:
    funções.escreva('MENU PRINCIPAL')
    print(f' {cores["Verde"]}1{cores["Sem"]} - {cores["Azul Escuro"]} Ver pessoas cadastradas {cores["Sem"]}')
    print(f' {cores["Verde"]}2{cores["Sem"]} - {cores["Azul Escuro"]} Cadastrar nova pessoa{cores["Sem"]}')
    print(f' {cores["Verde"]}3{cores["Sem"]} - {cores["Azul Escuro"]} Sair do sistema{cores["Sem"]}')
    print('-'*49)
    escolhas= [1,2,3]
    opção= funções.leiaInt('Sua opção')
    while opção not in escolhas:
        print(f'{cores["Vermelho"]}Digite uma opção válida!!!{cores["Sem"]}')
        break

    if opção == 1:
        funções.escreva('PESSOAS CADASTRADAS')
        sleep(0.5)
        try:
            with open('principal.txt', 'r' ,encoding= 'utf=8') as file:
                print(file.read())
                sleep(2)
        except:
            with open('principal.txt', 'x', encoding='utf=8') as file:
                print('Não existe Nenhum arquivo com esse nome')
                print('Mas não se preocupe, acabei de criar um para você!')

    elif opção == 2:
        funções.escreva('NOVO CADASTRO')
        sleep(0.5)
        try:
            with open('principal.txt','a',encoding="utf-8") as file:
                nome= str(input('Nome:'))
                idade= int(input('Idade:'))
                file.write(f'{nome:<15} \t')
                file.write(f'{idade:>20} anos \t \n')
                print(f'Novo registro de {nome} adicionado!')
                sleep(2)
        except:
            with open('principal.txt','x',encoding="utf-8") as file:
                print(f'Não existe nenhum arquivo com esse nome')
                print(f'Mas não se preocupe, acabei de criar um para você')
    elif opção == 3:
        print('Saindo...')
        sleep(2)
        print(f'{cores["Amarelo"]}-=-'*12)
        print(f'Obrigado por usar ;/')




