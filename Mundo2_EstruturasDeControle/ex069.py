idade2=0
homens=0
mulheres=0
print('-' * 40)
print('         CADASTRE UMA PESSOA')
print('-' * 40)
while True:
    idade= int(input('IDADE:'))
    sexo= ' '
    while sexo not in 'MF':
        sexo= str( input('SEXO {M/F]:')).upper().strip()
    print('-' *20)
    resposta= str( input('Quer continuar? [S/N]')).upper().strip()
    print('-' * 20)
    if idade > 18:
        idade2+=1
    if sexo == 'M':
        homens+=1
    if sexo == 'F' and idade < 20:
        mulheres+=1
    if resposta == 'N':
        break
print('--------FIM DO PROGRAMA---------')
print(f'\033[32mPESSOAS ACIMA DOS 18\033[m:[{idade2}]')
print(f'\033[34mHOMENS CADASTRADOS\033[m:[{homens}]')
print(f'\033[35mMULHERES ABAIXO DOS 20 ANOS\033[m:[{mulheres}]')