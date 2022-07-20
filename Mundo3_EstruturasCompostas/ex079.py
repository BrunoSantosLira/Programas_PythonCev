valores= []
while True:
        contador= int(input('Digite um valor na lista:'))
        if contador in valores:
            print('Valor já contabilizado!! Não será adicionado')
        else:
            valores.append(contador)
        resposta= str( input('Quer continuar? [S/N]')).upper()
        if resposta == 'N':
          print('Programa Finalizado')
          break
print(sorted(valores))



