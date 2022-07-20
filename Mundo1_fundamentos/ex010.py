real= float( input('Quantos Reais você tem na carteira? R%'))
dola= real / 4.67
euro= real / 5.04
iene= real / 0.036
print(f'Com R%{real:.2f} é possível comprar U${dola:.2f}')
print(f'Com R${real:.2f} é possivel comprar €{euro:.2f}')
print(f'Com R${real:.2f} é possível comprar ¥{iene:.2f}')