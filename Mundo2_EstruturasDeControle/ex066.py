soma=0
contador=0
while True:
    número= int( input('Digite um valor: '))
    if número == 999:
         break
    soma+=número
    contador+=1
print(f'No total, foram digitados {contador} números. Sendo que a soma entre eles é {soma}')