from datetime import date
nascimento= int( input('Data de Nascimento:'))
ano= date.today().year
idade= ano - nascimento
tempo = 18 - idade
tempo2= idade - 18
print(f'Quem nasceu em {nascimento} tem {idade} em {ano}')
sexo= input('Qual o seu gênero? [M/F]:')
if sexo== 'F':
    print('Você não precisa se alistar obrigatoriamente!"')
else:
 if idade < 18:
    anoalistamento = ano + tempo
    print('Ainda vai chegar sua hora de se alistar!')
    print(f'\033[34m Vá se preparando!\033[m faltam {tempo} anos para o seu alistamento \n Que deverá acontecer em \033[34m{anoalistamento}!\033[m"')
 elif idade > 18:
    print('Você já passou da data do seu alistamento')
    print(f'Você deveria ter se alistado há {tempo2} anos')
    print(f'Seu alistamento foi em {ano - tempo2}')
 else:
    print('Você devé se alistar \033[31m imediatamente!!!')