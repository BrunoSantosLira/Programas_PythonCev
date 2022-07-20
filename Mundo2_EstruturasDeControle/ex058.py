from random import randint
print('Sou seu computador...')
print('Vamos jogar?')
print('Eu pensei em um número entre 0 e 10 \n TENTE ADIVINHAR!!!')
computador= randint(0,10)
palpite=0
contador=0
while palpite != computador:
    contador+=1
    palpite= int( input('Qual o seu palpite?'))
    if palpite > computador:
       print('Menos...', end='')
    if palpite < computador:
       print('Mais...', end='')
print(f'Você acertou após {contador} tentativas, PARABENS!!!')