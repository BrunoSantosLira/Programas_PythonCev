import datetime
data= datetime.date.today().year
dados= {}

dados['nome']= str( input('NOME: '))
dados['Idade']= int(input('Data de nascimento: '))
dados['Idade']= data - dados['Idade']
dados['CTPS']=int(input('Carteira de Trabalho(0 não tem): '))
if dados['CTPS'] == 0:
    print(dados)
    for k,v in dados.items():
        print(f'{k} tem o valor de {v}')
else:
    dados['Contratação']= int(input('Ano de contratação: '))
    dados['Salário']= float(input('Salario: '))
    dados['Aposentadoria']= (dados['Contratação'] + 35 ) - (data - dados['Idade'])
    print('-=-'*20)
    print(dados)
    for k,v in dados.items():
        print(f'{k} tem o valor de {v}')
