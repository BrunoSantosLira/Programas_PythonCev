n1= int( input('Primeiro segmento:'))
n2= int( input('Segundo segmento:'))
n3= int( input('Terceiro segmento:'))
soma= n1+ n2
if soma > n3:
    print('É possível formar um triângulo!')
    if n1==n2 and n2==n3:
        print('TRIÂNGULO EQUILÁTERO')
    elif n1 != n2  !=n3 != n1:
        print('TRIÂNGULO ESCALENO')
    else:
        print('Escaleno')
else:
    print('Não é possível formar um triângulo')
