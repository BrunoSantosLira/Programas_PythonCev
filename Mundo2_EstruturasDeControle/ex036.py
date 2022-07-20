casa= float( input('Digite o valor da casa: R$'))
salário= float( input('Digite o salário do comprador: R$'))
anos= int( input('Quantos anos de financiamento? '))
parcelas= anos * 12
prestação= casa / parcelas
print(f'Para pegar uma casa no valor de R${casa:.2f} em {anos} anos, as prestações serão de R${prestação:.2f}')
porcentagem= salário / 100 * 30
if prestação > porcentagem:
    print('Financiamento \033[31m NEGADO \033[m ')
else:
    print('Financiamento \033[32m APROVADO \033[m')
