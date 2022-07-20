from math import pow
print('-=-' *20)
print('TABELA IMC')
print('IMC ABAIXO DE 18.5:ABAIXO DO PESO')
print('IMC ENTRE 18.5 E 25: PESO IDEAL')
print('IMC ENTRE 25 E 30: SOBREPESO')
print('IMC ENTRE 30 E 40: OBESIDADE')
print('IMC SUPERIOR A 40: OBERSIDADE MÓRBIDA')
print('-=-'*20)
peso= float( input('Digite o peso [KG]:'))
altura= float( input('Digite a altura [Metros]'))
IMC= peso / pow(altura,2)
print(f'Seu IMC é de {IMC:.1f}')
if IMC < 18.5:
    print('Classificação: ABAIXO DO PESO')
elif IMC < 25:
    print('Classificação: PESO IDEAL')
elif IMC < 30:
    print('Classificação: SOBREPESO')
elif IMC < 40:
    print('Classificação: OBESIDADE')
else:
    print('Classificação: \033[31m OBESIDADE MÓRBIDADA')

