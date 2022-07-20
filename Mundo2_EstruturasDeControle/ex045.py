from time import sleep
import random
print('Suas Opções:')
print('[ 0 ] PEDRA')
print('[ 1 ] PAPEL')
print('[ 2 ] TESOURA')
resposta= int( input('Qual a sua jogada?'))
computador= random.randrange(0,3)
if computador == 0:
    computador = 'PEDRA'
elif computador == 1:
    computador = 'PAPEL'
elif computador == 2:
    computador = 'TESOURA'

if resposta == 1:
    resposta = 'PEDRA'
elif resposta == 2:
    resposta = 'TESOURA'
elif resposta == 0:
    resposta = 'PEDRA'
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
print('\033[33m -=- \033[m'*10)
print(f'O computador jogou {computador}')
print(f'O jogador jogou {resposta}')
print('\033[33m -=- \033[m' * 10)
if computador== resposta:
    print('\033[34mJOGO EMPATADO \033[m')
else:
    if computador == 'PEDRA' and resposta == 'TESOURA':
        print('\033[31mCOMPUTADOR VENCEU \033[m')
    elif computador == 'PAPEL' and resposta== 'PEDRA':
        print('\033[31mCOMPUTADOR VENCEU \033[m ')
    elif computador == 'TESOURA' and resposta == 'PAPEL':
        print('\033[31m COMPUTADOR VENCEU \033[m')
    else:
        print('\033[33m jogador venceu \033[m')