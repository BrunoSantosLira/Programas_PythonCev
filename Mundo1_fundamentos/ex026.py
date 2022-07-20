frase= ( input('Digite uma Frase: ')).upper().strip()
Contador_a= frase.count('A')
Posição_a= '-' + frase
print(f'A letra \033[1;4m A \033[m aparece {Contador_a} vezes na frase')
print('A primeira letra \033[1;4m A \033[m apareceu na posição', Posição_a.find('A'))
print('A última letra \033[1;4m A \033[m apareceu na posição', Posição_a.rfind('A'))

#frase= input('Digite uma frase:').strip().split()
#print(frase[2].find('a'))