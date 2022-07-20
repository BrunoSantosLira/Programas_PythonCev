'''from random import sample
n1= input('Primeiro Aluno:')
n2= input('Segundo Aluno:')
n3= input('Terceiro Aluno:')
n4= input('Quarto Aluno:')
lista= sample([n1,n2,n3,n4],k=4)
print(f'A ordem de apresentação será: \n{lista}')'''

from random import shuffle
n1= input('Primeiro aluno:')
n2= input('Segundo aluno:')
n3= input('Terceiro aluno:')
n4= input('Quarto Aluno:')
lista= [n1,n2,n3,n4]
shuffle(lista)
print(f'A ordem de aparição foi{lista}')
