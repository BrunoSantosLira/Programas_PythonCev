
while True:
    número= int ( input('Digite um número para ver sua tabuada (número negativo para sair): '))
    c=1
    if número < 0:
        break
    print('=' * 18)
    while c < 11:
         print(f'{número} X {c} = {número * c}')
         c+=1
    print('=' * 18)
print('\033[31m TABUADA FINALIZADA')