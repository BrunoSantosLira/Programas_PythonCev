lista=[]
m=0
notas=0
resp=0
while True:
    nome= str( input('NOME:'))
    N1= float( input('NOTA 1:'))
    N2= float( input('NOTA 2:'))
    m= (N1 + N2) / 2
    lista.append([nome,[N1,N2],m])
    resposta= str(input('Quer continuar? [S/N]')).upper()
    if resposta == 'N':
        break

print('-='*10)
print('BOLETIM')
print(f' {"N²":<4} {"NOME":<10} {"MÉDIA":<10} ')
for i,p in enumerate(lista):
    print(f'{i:<4} {p[0]:<10}  {p[2]:<10}')

while True:
    mostrar= int( input('Deseja mostrar a nota de qual aluno? (Aperte 999 para parar)'))
    if mostrar == 999:
        break
    else:
        print(f'Notas de {lista[mostrar][0]}: {lista[mostrar][1]}')



