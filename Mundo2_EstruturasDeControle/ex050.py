s=0
contador=0
for c in range(1,7):
    n= int( input(f'Digite o {c}² valor '))
    if n % 2 == 0:
        s+=n
        contador+=1
print(f'Dos {contador} valores pares digitados, a soma entre eles é {s}')