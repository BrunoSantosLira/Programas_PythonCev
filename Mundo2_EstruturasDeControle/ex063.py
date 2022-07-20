print('-=-' * 12)
print('SÊQUENCIA DE FIBONACCI')
print('-=-' * 12)
termos= int ( input('Quantidade de termos'))
t1=0
t2=1
c=0
print(t1, end=' - ')
print(t2, end=' - ')
while c < termos - 2:
    t3= t1 + t2
    print(t3, end=' - ')
    t1=t2
    t2=t3
    c+=1
print('FIM DA SEQUÊNCIA')

