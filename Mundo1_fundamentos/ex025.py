nome=input('Qual é o seu nome completo? ').upper()
nome2= nome.split()
print(f'Seu nome tem \033[35m Silva? \033[m','SILVA' in nome2[0:])