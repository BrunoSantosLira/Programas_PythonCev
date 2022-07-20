from time import sleep
print ('-=-' * 10)
print('ANALISADOR DE TRIÂNGULOS')
print('-=-' * 10)

primeiro= float( input('Digite o primeiro segmento:'))
segundo= float( input('Digite o segundo segmento:'))
terceiro= float( input('Digite o terceiro segmento:'))
print('FAZENDO TODOS OS CALCULOS...')
sleep(1.5)
soma= primeiro + segundo
if soma > terceiro:
    print('Os segmentos acima PODEM formar um TRIÂNGULO!')
else:
    print('OS segmentos acima NÃO PODEM formar um TRIÂNGULO!')