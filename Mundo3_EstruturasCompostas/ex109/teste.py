from ex109 import moeda

preço= float(input('Digite um preço:'))
print(f' A metade do número {moeda.moeda(preço)} é {moeda.metade(preço,True)}')
print(f'O dobro do número {moeda.moeda(preço)} é {moeda.dobro(preço,False)}')
print(f'Aumentando 10%, temos {moeda.aumentando(preço,10,False)}')
print(f'Diminuindo 13%, temos {moeda.reduzindo(preço,13,False)}')