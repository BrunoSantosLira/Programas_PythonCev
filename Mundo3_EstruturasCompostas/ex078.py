#Do meu jeito
'''valores= []
for c in range(0,5):
    valores.append(int(input(f'Digite o valor para a posição {c}:')))
print('-='*15)
print(f'Você digitou a seguinte lista: {valores}')
print(f'Sendo que o maior valor dessa lista foi: {max(valores)}, aparecendo nas posições {valores.index(max(valores))}')
print(f'Enquanto o menor foi: {min(valores)}, aparecendo nas posições {valores.index(min(valores))}')'''

#Jeito do Professor

valores= []
maior=0
menor=0
for c in range(0,5):
    valores.append(int(input(f'Digite o valor para a posição {c}')))
    if c == 0:
        maior= menor= valores[c]
    else:
        if valores[c] > maior:
            maior= valores[c]
        if valores[c] < menor:
            menor= valores[c]

print('='*12)
print(valores)
print(f'O maior valor foi: {maior}, sendo que o mesmo apareceu em:')
for pos, v in enumerate(valores):
    if v == maior:
        print(f'{pos}...')
print(f'Enquanto o menor foi : {menor}, sendo que o mesmo aparceu em:')
for pos, v in enumerate(valores):
    if v == menor:
        print(f'{pos}...')
print('-='*12)