
contagem= ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
while True:
    c= int( input('Digite um número entre 0 e 20:'))
    while not c <= 20:
        c= int( input('Tente Novamente. Digite um número entre 0 e 20 novamente:'))
    print(f' O número que você digitou é {contagem[c]}')
    resposta= str( input('Vocêr quer continuar? [N/S]')).upper()
    if resposta == 'N':
        break
print('\033[31m PROGRAMA FINALIZADO')
