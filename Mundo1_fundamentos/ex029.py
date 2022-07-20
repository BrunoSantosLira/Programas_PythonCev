velocidade= float( input('Qual a velocidade atual do carro? '))
multa= (velocidade - 80) * 7
if velocidade <= 80:
    print('Tenha um Bom dia! Dirija com segurança')
else:
    print('\033[31;1;4m MULTADO! \033[m Você excedeu o limite permitido de 80km/h!')
    print(f'Você deve pagar uma multa de \033[31m R${multa}!!!')