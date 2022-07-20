from time import sleep

def contador(início,fim,passo):
    print('-=-'*15)
    if passo == 0:
        passo = 1

    if passo < 0:
        passo = abs(passo)

    if início < fim:
        for c in range(início,fim,passo):
            print(c,end=' ')
            sleep(0.5)
        print('FIM!')

    elif início >= fim:
        print(início,end=' ')
        while início > fim:
            início -= passo
            print(início,end=' ')
            sleep(0.3)
        print('FIM! ')



contador(início=1, fim=10+1, passo=1)
contador(início=10, fim=0, passo=2)
print('Agora chegou sua vez de contar! vamos lá?')
início= int(input('INÍCIO:'))
fim= int(input('FIM:'))
passo= int(input('PASSO:'))
contador(início,fim,passo)
