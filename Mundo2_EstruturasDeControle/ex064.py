resposta = cont = soma = 0
while resposta != 999:
    resposta= int( input('Digite um número inteiro[999 para parar]'))
    if resposta != 999:
        soma+=resposta
        cont+=1
print(f'Houve um total de {cont} números digitados, sendo que a soma desses números é {soma} ')