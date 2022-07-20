termo= int(input('Digite o primeiro termo'))
razão= int(input('Digite a razão'))
meio= termo + (10-1)* razão
for c in range (termo,meio+ razão,razão):
    print(c, end=' - ')
print('ACABOU', end=' ')