nome= input('Digite seu nome completo:').split()
print('Prazer em te conhecer!')
print('Seu primeiro nome é \033[33m', nome[0])
print(' \033[m Seu último nome é \033[34m', nome[-1])