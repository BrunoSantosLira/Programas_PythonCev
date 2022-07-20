lista  = []
listaP = []
listaI = []
while True:
    valor= int( input('Digite um número:'))
    lista.append(valor)
    if valor % 2 == 0:
        listaP.append(valor)
    else:
        listaI.append(valor)
    resposta= str( input('Quer continuar? [S/N]')).upper()
    if resposta == 'N':
        break
print('-=-'*20)
print(f'Todos os valores digitados: {lista}')
print(f'Valores pares: {listaP}')
print(f'Valroes ímpares: {listaI}')
