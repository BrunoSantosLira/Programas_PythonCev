matriz= [[0,0,0],[0,0,0],[0,0,0]]
totpar=0
coluna=0
linha= 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c]= int( input(f'Digite um valor para a posição {l,c}'))
        if matriz[l][c] % 2 == 0:
            totpar += matriz[l][c]

for l in range(0,3):
    for c in range(0,3):
        print(f'({matriz[l][c]})',end=' ')

    print()

for l in range(0,3):
    if matriz[l][2]:
        coluna += matriz[l][2]

'''linha= max(matriz[1])'''

#ou

for c in range(0,3):
    if c == 0:
        maior=matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print('-='*12)
print(f'A soma dos valores pares é : {totpar}')
print(f'A soma dos valores da terceira coluna é : {coluna}')
print(f'O maior valor da segunda linha é: {maior}')

