lista = []
while True:
    lista.append(int(input('Digite um valor:')))
    resposta= str(input('Quer continuar? [S/N]')).upper()
    if resposta == 'N':
        break
print('-=' *10 )
print(f'Você Digitou {len(lista)} valores')
print(f'Ordem decrescente: {sorted(lista, reverse = True)}')
if 5 in lista:
    print('O valor 5 está na lista')
else:
    print('O valor 5 não está presente na lista')