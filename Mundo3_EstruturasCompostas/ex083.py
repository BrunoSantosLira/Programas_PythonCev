'''lista= []
expressão= str(input('Digite a expressão numérica:'))
p1= expressão.count('(')
p2= expressão.count(')')
if p1 != p2 or p2 != p1:
    print('\033[31mExpressão Inválida!!!!\033[m')
else:
    print('\033[32m Expressão Válida \033[m')'''

expressão= str( input('Digite um valor:'))
pilha= []
for simb in expressão:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Operação válida')
else:
    print('Expressão inválida')

