frase= input('Digite uma frase').upper().replace(' ','')
reverso= frase[::-1]
print(frase)
print(f'O inverso de {frase} é {reverso}')
if frase == reverso:
    print('Está frase é um polímetro')
else:
    print('Está frase não é um polímetro')
