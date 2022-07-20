lista=('lápis',   ' 1.75', 'Borracha',     ' 2.00','Caderno',  ' 15.90',
       'Estojo',  ' 25.00' ,'Transferidor',' 4.20','Compasso', ' 9.99',
       'Mochila', ' 120.32','Canetas',     ' 22.30','Livro',   ' 34.90')
print('-='*30)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-='*30)
for pos, c in enumerate(lista):
        if pos % 2 == 0:
            print(f'{c:.<30}',end='')
        else:
            print(F'R${c}')
print('-'*35)



