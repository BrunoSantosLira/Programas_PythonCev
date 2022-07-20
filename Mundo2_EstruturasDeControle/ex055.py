pesomaior=0
pesomenor=0
for c in range(1,4):
    peso= float( input(f'Digite o peso da {c} pessoa:'))
    if c == 1:
        pesomaior= peso
        pesomenor=peso
    else:
        if peso > pesomaior:
         pesomaior= peso
        if peso < pesomenor:
         pesomenor= peso

print('\033[35m DENTRE ESSES PESOS: \033[35m')
print('\033[33m = \033[m'*20)
print(f'O maior peso foi {pesomaior}')
print(f' Enquanto o menor foi {pesomenor}')
print('\033[33m = \033[m'*20)