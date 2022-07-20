from random import randint
vitórias=0
print('=' *20)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('=' *20)
while True:
    jogador= int( input('Digite um número: '))
    resposta= str( input('Você escolhe Par ou Impar? [P/I]')).upper().strip()
    print('=' * 20)
    computador= randint(0,10)
    soma= computador + jogador
    if soma % 2 == 0:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} \n o que resulta em Par')
        print('='*20)
        if resposta == 'P':
            print('\033[33m Você Venceu! \033[m')
            vitórias+=1
        else:
            print('\033[31m Você Perdeu... \033[m')
            break
    if soma % 2 == 1:
        print(f'Você jogou {jogador} e o computador {computador}. Total de {soma} \n o que resulta em Ímpar ')
        if resposta == 'I':
            print('\033[33m Você Venceu! \033[m')
            vitórias+=1
        else:
            print('\033[31m Você Perdeu \033[m')
            break
print('=' * 20)
print(f'\033[31m GAME OVER \033[m \n Vitórias consectivas: {vitórias} ')
