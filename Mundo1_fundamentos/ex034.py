from time import sleep
salário= float( input('Qual é o salário do funcionário?: R$'))
print('\033[31m CALCULANDO... \033[m')
sleep(2)
if salário <= 1250.00:
    salárioNovo= salário / 100 * (100 + 15)
    print(f'Uma pessoa que antes recebia \033[1;32m R${salário:.2f}, \033[m Agora com 15% de aumento receberá \033[34m R${salárioNovo:.2f}')
else:
    salárioNovo= salário / 100 * (100 + 10)
    print(f'Uma pessoa que antes recebia \033[32m R${salário:.2f} \033[m, Agora com 10% de aumento receberá \033[34m R${salárioNovo:.2f}')