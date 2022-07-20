import random
from time import sleep
print('-------------------------')
print('   JOGO NA MEGA SENA')
print('-------------------------')
jogos=int (input('Quantos jogos serão digitados?'))
for c in range(0,jogos):
    lista= []
    while len(lista) != 6:
        resultado= random.randint(1,61)
        if resultado not in lista:
            lista.append(resultado)

    print(f' jogo {c+1}: {lista}')

