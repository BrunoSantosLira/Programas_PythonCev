from time import sleep
numero= int(input('Digite um número: '))
print('\033[35m PROCESSANDO... \033[m')
sleep(1.5)
if numero % 2 == 0:
    print('Esse número é \033[34m Par \033[m')
else:
    print('Esse número é \033[31m Ímpar \033[m')