from datetime import date
ano= int( input('Que ano você quer analisar? Digite 0 para ver a análise do ano atual:'))
if ano == 0:
    ano= date.today().year
if ano % 100 == 0:
    if ano % 400 == 0:
        print(f'O ano de {ano} é \033[36m BISSEXTO! \033[m')
    else:
        print(f'O ano de {ano} NÃO é \033[31m BISSEXTO \033[m')
else:
 if ano % 2 == 0:
        print(f'O ano de {ano} é \033[36m BISSEXTO! \033[m')
 else:
        print(f'O ano de {ano} NÃO é \033[31m BISSEXTO! \033[m')


