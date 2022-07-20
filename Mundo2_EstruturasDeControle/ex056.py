soma=0
média=0
contador=0
idademaior=0
for PESSOA in range(1,5):
    print(f'---- {PESSOA}² PESSOA -------')
    nome= input(('NOME:')).upper().strip()
    idade= int( input('IDADE:'))
    sexo= input('SEXO [M/F]:').upper()
    soma+= idade
    if sexo== 'M' and idade > idademaior:
     idademaior=idade
     nomemaior=nome
    if sexo == 'F' and idade < 20:
        contador+=1
média= soma / 4
print(f'A média de idade entre eles é de: {média:.1f}')
print(f'O homem mais velho tem {idademaior} anos e se chama {nomemaior}')
print(f'Ao todo são {contador} mulheres abaixo dos 20 anos')