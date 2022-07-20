dados={}
pessoas=[]
total=0
mulheres=[]
acima=[]
while True:
    dados['nome']= str(input('NOME: '))
    dados['sexo']= str(input('SEXO[M/F]: ')).upper()
    if dados['sexo'] == 'F':
        mulheres.append(dados['nome'])
    dados['idade']= int( input('IDADE: '))
    total += dados['idade']
    pessoas.append(dados.copy())
    resposta=str(input('Quer continuar? [S/N]: ')).upper()
    if resposta == 'N':
        break

print('-=-'*18)
print(f'Quantidade de pessoas cadastradas: {len(pessoas)}')
média= total / len(pessoas)
print(f'Média de idade = {média}')
print(f'Mulheres cadastradas: {mulheres}')
print('Lista de pessoas que estão acima da média:')
for d in pessoas:
    if d['idade'] >= média:
        print(d)
