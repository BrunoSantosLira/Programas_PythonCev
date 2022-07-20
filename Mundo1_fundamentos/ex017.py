'''import math
catetoP= float ( input('Cateto Oposto:'))
catetoA= float ( input('Cateto Adjente:'))
soma= (math.pow(catetoP,2)) + (math.pow(catetoA,2))
raizquadrada= math.sqrt(soma)
print(f'A hipotenusa mede {raizquadrada:.2f}')'''

from math import hypot
catetoP= float( input('Cateto Oposto:'))
catetoA= float( input('Cateto Adjente:'))
hipotenusa= hypot(catetoP,catetoA)
print(f'A hipotenusa é igual a {hipotenusa:.2f}')