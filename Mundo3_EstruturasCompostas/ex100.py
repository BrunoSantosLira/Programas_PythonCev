from random import randint
from time import sleep

def sorteia(sorteio):
    sorteados=[]
    for c in range(0,5):
        sorteio= randint(0,10)
        print(sorteio,end=' ')
        sleep(0.3)
        sorteados.append(sorteio)
    números.append(sorteados)
    print('PRONTO!')


def somapar(lista):
    totalpar=0
    for cont in lista:
        if cont % 2 == 0:
            totalpar += cont
    print(totalpar)


print('Sorteando 5 números da lista...')
sleep(1)
números= []
sorteia(números)
print('-=-'*15,)
for c in números:
    print(c,end='')
    print()
print('A soma dos valores pares é:',end=' ')
somapar(c)



