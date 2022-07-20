#Fazendo de maneira bruta
'''n1= int( input('Digite o primeiro valor:'))
n2= int( input('Digite o segundo valor:'))
n3= int( input('Digite o terceiro valor:'))

if n1>n2>n3:
    print(f'O maior número é {n1}')
if n2>n1>n3:
    print(f'O maior número é {n2}')
if n3>n2>n1:
    print(f'O maior número é {n3}')

if n1<n2<n3:
    print(f'O menor número é {n1}')
if n2<n1<n3:
    print(f'O menor número é {n2}')
if n3<n2<n1:
    print(f'O menor número é {n3}')'''

#Com lista utilizando max e min
n1= int(input('Digite o primeiro número:'))
n2= int(input('Digite o segundo número: '))
n3= int(input('Digite o terceiro número:'))
lista= [n1,n2,n3]
print(f'O maior número é \033[34m{max(lista)}\033[m')
print(f'O menor número é \033[31m{min(lista)}')