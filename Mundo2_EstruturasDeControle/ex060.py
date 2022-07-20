'''fator=1
contador=1
número= int( input('Digite um número para ver seu fatorial'))
for contador in range(número,1,-1):
    fator*= contador
print(f'O fatorial desse número é: {fator}')'''

f=1
num= int(input('Digite um número para ver o seu fatorial'))
c= num
print(f'CALCULADO FATORIAL DE {num}! =',end=' ')
num+=1
while c > 0:
    f*=c
    c-=1
    print(num, end=' x ')
print(f'O resultado obtido foi de {f}')