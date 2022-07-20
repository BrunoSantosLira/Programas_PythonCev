
from ex108 import moeda

preço= float(input('Digite um preço:'))
print(f' A metade de {moeda.moeda(preço)} é {moeda.moeda(moeda.metade(preço))} ')
print(f' O dobro de {moeda.moeda(preço)} é {moeda.moeda(moeda.dobro(preço))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentando(preço,10))}')