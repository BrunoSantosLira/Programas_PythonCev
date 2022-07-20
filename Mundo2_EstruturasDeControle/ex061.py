print('''-----------------------
DEZ PRIMEIROS TERMOS DE UMA P.A
-------------------------------''')
c=0
termo= int( input('Digite o termo:'))
razão= int( input('Digite a razão:'))
while c < 10:
    c+=1
    print(termo,end=' - ')
    termo+=razão
print('ACABOU')