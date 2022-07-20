from datetime import date
ano= date.today().year
maior=0
menor=0
for c in range(1,8):
    nascimento= int( input(f'Digite a data de nascimento da {c}² pessoa'))
    idade= ano - nascimento
    if idade >= 21:
         maior+=1
    else:
         menor+=1
print(f'Ao todo, existem {maior} pessoas maiores de idade')
print(f'E apenas {menor} pessoas menores de idade ')