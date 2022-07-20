from datetime import date
print('\033[33m-=- \033[m' * 20)
print('C O N F E D E R A Ç Ã O   N A C I O N A L')
print('\033[33m -=- \033[m' *20)
ano_nascimento= int( input('Digite o ano de nascimento do atleta:'))
ano= date.today().year
idade= ano - ano_nascimento
print(f'O atleta possuí {idade} anos')
if idade <= 9:
    print('Classificação: \033[34m MIRIM \033[m')
elif idade <= 14:
    print('Classificação: \033[32m INFANTIL \033[m')
elif idade <= 19:
    print('Classificação: \033[31m JÚNIOR \033[m')
elif idade <= 25:
    print('Classificação: \033[35m SÊNIOR \033[m')
else:
    print('Classificação: \033[33m MASTER \033[m')