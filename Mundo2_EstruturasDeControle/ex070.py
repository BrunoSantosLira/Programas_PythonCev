mil=0
total= 0
contador= 0
menorN=0
menorP=0
print('-'*15)
print('Loja DE Tudo')
print('-'*15)
while True:
    nome= str( input('Digite o nome do produto: '))
    preço= int( input('Digite o preço: R$'))
    contador+=1
    print(contador)
    total+=preço
    if contador == 1:
       menorP=preço
       menorN=nome
    if menorP > preço:
        menorN=nome
    if preço >1000:
        mil+=1
    resposta= str( input('Quer Continuar? [S/N]')).upper().strip()
    if resposta == 'N':
        break
print('--------FIM DO PROGRAMA----------')
print(f'Total de gastos : RS{total}')
print(f'Produtos acima de 1000 reais: {mil}')
print(f'{menorN} é o produto mais barato')

