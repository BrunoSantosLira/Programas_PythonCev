'''viagem = float( input('Qual a distância da sua viagem?'))
print(f'Você está prestes a fazer uma viagem de {viagem}km')
if viagem <= 200:
    viagem1= viagem * 0.50
    print(f'E o preço da sua passagem será de R${viagem1:.2f}')
else:
    viagem2= viagem * 0.45
    print('Sua viagem entre em nossa faixa de desconto!')
    print(f'Sua passagem custará R${viagem2:.2f} ')'''

#simplificado
viagem= float( input('Qual a distância da sua viagem? '))
print(f'Você está prestes a fazer uma viagem de \033[33m {viagem}km \033[m')
preço= viagem * 0.50 if viagem <= 200 else viagem * 0.5
print(f'Sua viagem custará \033[34mR${preço:.2f}')
