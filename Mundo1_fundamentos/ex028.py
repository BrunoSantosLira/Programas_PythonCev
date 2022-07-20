import random
from time import sleep
print( '\033[33m' '-=-' *20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
print('\033[31m PROCESSANDO...')
sleep(2)
numeropc= int(random.randrange(0,5))
resposta= int( input(' \033[m Em que número eu pensei? '))

if numeropc == resposta:
    print(' \033[32m Você ganhou!')
    print(f'Eu realmente tinha pensado no número {numeropc}')
else:
    print('\033[34m Ganhei! Ganhei! \033[m')
    print(f'Eu pensei no número {numeropc}')
print("\033[32m Obrigado por jogar comigo!! ;/")