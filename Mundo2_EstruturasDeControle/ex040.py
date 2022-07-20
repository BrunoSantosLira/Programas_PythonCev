'''n1= float( input('Digite a primeira nota:'))
n2= float( input('Digite a segunda nota:'))
média = (n1+n2) / 2
print(f'Você tem uma média de {média}')
if média < 5:
    print(f'Situação: \033[31m REPROVADO \033[m')
elif média >= 5 and média < 6.9:
    print(f'Situação: \033[33m RECUPERAÇÃO \033[m')
elif média >= 7:
    print(f'Situação: \033[32m APROVADO \033[m')'''

n1= float( input('Digite a primeira nota:'))
n2= float( input('Digite a segunda nota:'))
média= (n1+n2) / 2
print(f'O aluno está com média {média}')
if média < 5 :
    print('Situação: \033[31m APROVADO \033[m')
elif média >= 7:
    print('Situação : \033[32m APROVADo \033[m ')
else:
    print('Situação: \033[33m RECUPERAÇÃO \033[m')
    notarec= float( input ('Digite a nota da sua recuperação:'))
    médiafinal= (notarec + média) / 2
    if médiafinal >= 7:
     print('O aluno passou na recuperação')
    else:
     print('Aluno \033[31m REPROVADO \033[m ')

