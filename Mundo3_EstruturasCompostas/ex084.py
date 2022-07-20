galera= []
pessoas=[]
maior=menor=0
while True:
        pessoas.append(str(input('NOME:')))
        pessoas.append(float( input('PESO:')))
        if len(galera) == 0 :
            maior=menor=pessoas[1]
        else:
            if pessoas[1] > maior:
                maior= pessoas[1]
            if pessoas[1] < menor:
                menor=pessoas[1]
        galera.append(pessoas[:])
        pessoas.clear()
        resposta= str( input('Quer continuar? [S/N]')).upper()
        if resposta == 'N':
            break
print(galera)
print('-='*20)
print(f'No total, foram cadastradas {len(galera)} pessoas')
print(f'O maior peso digitado foi: {maior}. De',end= '')
for  c in galera:
    if c[1] == maior:
        print(f' {c[0]}... ')
print(f'Enquanto o menor foi: {menor}. De ', end= '')
for c in galera:
    if c[1] == menor:
        print(f'{c[0]}...')
