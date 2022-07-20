termo= int ( input('Digite o primeiro Termo: '))
razão= int ( input('Digite a razão: '))
c=0
PrimeiraPA=10
while c < PrimeiraPA:
    print(termo, end=' - ')
    termo+=razão
    c+=1
    if c == PrimeiraPA:
     mais= int ( input('Quantos termos você quer adicionar a mais?'))
     PrimeiraPA += mais
print('ACABOU')