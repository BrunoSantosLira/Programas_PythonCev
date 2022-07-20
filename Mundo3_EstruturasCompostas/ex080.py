lista = []
for c in range(0,5):
    valor = int ( input('Digite um valor:'))
    if c == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Valor adicionado na última posição da lista')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print(f'Valor adicionado na posição {pos} da lista')
                break
            pos+=1
print('-='*18)
print(f'Os valores adicionados em ordem são:{lista}')