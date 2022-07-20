golsLista=[]
jogador={}
time=[]
while True:
    golsLista.clear()
    jogador['nome']= str( input('NOME:'))
    partidas= int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    for partida in range(0,partidas):
        golsLista.append(int(input(f'Quantos gols na partida {partida}?')))
        jogador['gols']= golsLista[:]
        jogador['Total']= sum(golsLista)
    time.append(jogador.copy())
    while True:
        resposta= str(input('Quer continuar? [S/N]:')).upper()[0]
        if resposta in 'SN':
            break
        print('ERRO!!! DIGITE UMA RESPOSTA VÁLIDA!')
    if resposta == 'N':
        break

print('\033[33m-=-\033[m'*20)
print('====RESULTADOS====')
print(f' {"COD":<8} {"NOME":<8} {"GOLS":<8}     {"TOTAL":<15}')
for i,p in enumerate(time):
    print(f'{i:>2}',end=' ')
    for k,v in p.items():
        print(f'{str(v):<15}',end=' ')
    print()


while True:
    mostrar= int(input('Deseja fazer o levantamento de qual jogador?(999 para parar):'))
    if mostrar == 999:
        break
    if mostrar >= len(time):
        print('ERRO!!! não existe nenhum jogador com esse código')
    else:
        print('\033[33m-\033[m '*30)
        print(f'Levantamento do jogador {time[mostrar]["nome"]}:')
        for i,g in enumerate(time[mostrar]['gols']):
            print(f'No jogo {i+1} ele fez {g} gol(s)')
        print('\033[33m-\033[m'*30)
print()
print('=====PROGRAMA FINALIZADO=====')
