from ex107 import moeda


preço= float(input('Digite o preço: R$'))
print('-=-'*20)
print(f'A metade de {preço} é {moeda.metade(preço)}')
print(f'O dobro de {preço} é {moeda.dobro(preço)}')
print(f'Aumentando 10%, temos {moeda.aumentando(preço,10)}')
print(f'Reduzindo 13%, temos {moeda.reduzindo(preço,13)}')