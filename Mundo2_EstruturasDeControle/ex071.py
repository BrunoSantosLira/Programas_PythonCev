print('=' *15)
print('BANCO S.A')
print('=' *15)
valor= int( input('Digite o valor que deseja sacar? R$'))
print(f'Total de cédulas de R$50: {valor // 50}')
valor20= valor % 501
print(f'Total de cédulas de R$20: {valor20 // 20}')
valor10= valor20 % 20
print(f'Total de cédulas de R$10: {valor10 // 10}')
valor1= valor10 % 10
print(f'Total de moedas de R$1: {valor1 // 1}')