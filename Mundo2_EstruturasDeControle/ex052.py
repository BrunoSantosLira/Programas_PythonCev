num= int( input('Digite um número inteiro:'))
contador=1
for c in range(1,num+1):
    print(c,end=' ')
    if num % c == 0:
     contador+=1
contador-=1
if contador == 2:
    print(f'\nO número {num} é primo, pois só foi dívisível {contador} vezes')
else:
    print(f'\nO número {num} NÃO é primo, pois foi divisível {contador } vezes')