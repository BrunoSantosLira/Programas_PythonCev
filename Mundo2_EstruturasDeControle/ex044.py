print('\033[33m ========= MERCADINHO BARATEIRO ============= \033[m')
preço=float( input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] á vista dinheiro/cheque')
print('[ 2 ] á vista no cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão(possuí juros)')
opção= int( input('Qual opção?'))
if opção == 1:
    desconto= preço / 100 * (100 - 10)
    print('Pagando à vista o cliente ganha 10% de desconto ')
    print(f'Preço Final: {desconto}')
elif opção == 2:
    desconto= preço / 100 * (100 - 5)
    print('Pagando à vista no cartão o cliente ganha 5% de desconto')
    print(f'Preço Final: {desconto}')
elif opção == 3:
    parcelamento= preço / 2
    print(f'Sua compra será parcelada em 2x no cartão, cada parcela custará R${parcelamento}')
elif opção == 4:
    juros= preço / 100 * (100 + 20)
    parcelas= int( input('Em Quantas Parcelas?'))
    parcelamento= juros / parcelas
    print(f'Sua compra será parcelada em {parcelas}x no cartão, sendo que cada parcela custará R${parcelamento} COM JUROS')
    print(f'O preço total será: R${juros}')
else:
    print('Opção inválida')