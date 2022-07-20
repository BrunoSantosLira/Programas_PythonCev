def ficha(nom= '<desconhecido',g=0):
    print(f'O jogador {nom} fez {g} gols(s) no total')

nome= str(input('NOME DO JOGADOR:'))
if nome=='':
    nome='<desconhecido>'
gols= str(input('TOTAL DE GOLS:'))
if gols.isnumeric():
    gols=int(gols)
else:
    gols=0

ficha()
