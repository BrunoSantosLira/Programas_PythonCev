from time import sleep
número= int( input('Digite um número inteiro'))
resp= int( input('Escolha uma das bases para conversão: \n [ 1 ] Para \033[32m Binário \033[m  \n [ 2 ] para \033[33m Octadecimal \033[m \n [ 3 ] para \033[31m Hexadecimal \033[m \n Sua opção: '))
print('\033[31m FAZENDO CONVERSÃO \033[m')
sleep(1.5)
if resp== 1:
    binário= bin(número)
    print(f'{número} em \033[32m binário \033[m é {binário [2:]}')
elif resp== 2:
    octal= oct(número)
    print(f'{número} em \033[33m OctaDecimal \033[m é {octal[2:]}')
elif resp== 3:
    hexa= hex(número)
    print(f'{número} em \033[31m HexaDecimal \033[m é {hexa[2:]}')
else:
    print('\033[31m CONVERSÃO FALHADA \033[m \n Por favor, escolha uma opção disponível')