resposta=1
contador=0
soma=0
média=0
maior=0
menor=0
while resposta != 'N':
    número= int( input('Digite um número inteiro'))
    resposta= input('Quer continuar? [S/N]').upper().strip()
    contador+=1
    soma+=número
    if contador == 1:
        menor=número
    if número > maior:
        maior= número
    if número < menor:
        menor= número
média= soma / contador
print(f'Foram digitados {contador} valores, sendo que a média entre eles é de {média}')
print(f'E dentre eles o maior é {maior} e o menor é {menor}')