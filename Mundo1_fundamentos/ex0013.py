salário= float( input('Qual o salário do funcionário? R$'))
aumento= float( input('Quanto será o aumento? R$'))
novo= salário / 100 * (100 + aumento)
print(f'Um funcionário que antes recebia R${salário}, agora com {aumento}% de aumento irá receber R${novo:.2F}')