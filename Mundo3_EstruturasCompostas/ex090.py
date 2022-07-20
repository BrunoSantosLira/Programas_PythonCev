dados= {}
dados['NOME']= str(input('NOME DO ALUNO: '))
dados['MÉDIA']= float(input('MÉDIA DO JOGADOR: '))
print('-='*20)
if dados['MÉDIA'] >= 6:
    dados['SITUAÇÃO']= 'APROVADO(a)'
else:
    dados['SITUAÇÃO']= 'REPROVADO(a)'

for k,v in dados.items():
    print(f'{k} é igual a {v}')
