from random import randint
from time import sleep
from operator import itemgetter
resultados= {}

print('Valores Sorteados:')
for jogador in range(1,5):
    resultados[f'jogador {jogador}']= randint(1,6)

ranking= []
for k,v in resultados.items():
    print(f'=>{k} tirou '
          f'{v}')
    sleep(1)
ranking=sorted(resultados.items(), key=itemgetter(1),reverse=True)
print(ranking)
print('-=-'*20)
print('====RANKING====')

for i,v in enumerate(ranking):
    print(f'{i+1}² lugar: {v[0]} = {v[1]}')
    sleep(1)