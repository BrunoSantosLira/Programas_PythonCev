dados= {}
total=0
gols=0
golsLista= []

dados['Nome']= str(input('Nome do jogador:'))
partidas= int( input('Quantas partidas ele jogou?'))
for partida in range(0,partidas):
    gols= int(input(f'Quantos gols na partida{partida}?'))
    total += gols
    golsLista.append(gols)
    dados['Gols']= golsLista
    dados['Total']= total
print('-=-'*20)
print(dados)
print('-=-'*20)
for k,v in dados.items():
    print(f'O campo {k} tem valor {v}')
print('-=-'*20)
print(f'O jogador {dados["Nome"]} fez {partidas} partidas ')

for partida,gol in enumerate(golsLista):
    print(f'=>  Na partida {partida}, o jogador fez {golsLista[partida]} gols')
print(f'Um total de {dados["Total"]} gols ')


