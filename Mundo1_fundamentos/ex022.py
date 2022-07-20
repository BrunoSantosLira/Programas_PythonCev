nome= input('Digite seu nome:')
qnome= nome.split()
espaços= nome.count(' ')
quantidade_de_letras= len(nome) - espaços
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {quantidade_de_letras} letras')
print(f'Seu primeiro nome é {qnome[0]} e ele possuí {len(qnome[0])} letras')


