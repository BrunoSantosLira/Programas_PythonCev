n= input('Digite algo; ')
print('O tipo primitivo desse valor é', type(n))
print('Só tem espaço? ', n.isspace())
print('É um número?', n.isnumeric())
print('É alfabético?', n.isalpha())
print('É alfanúmero?', n.isalnum())
print('Está em maiúscula?', n.isupper())
print('Está em minúscula?', n.islower())
print('Está capitalizada?', n.istitle())