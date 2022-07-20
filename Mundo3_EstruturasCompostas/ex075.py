todos = ( int( input('Digite um valor: ')), int( input('Digite um valor: ')),
                                            int(input('Digite um valor: ')),
                                             int(input('Digite um valor: ')))
print(f'O valor 9 aparece {todos.count(9)} vezes')
if 3 in todos:
    print(f'O valor 3 aparce pela primeira vez na posição {todos.index(3)+1}²')
else:
    print('O valor 3 não foi digitado')
print(f'Valores pares digitados:',end=' ')
for c in todos:
    if c % 2 == 0:
        print(c, end=' ')