s=0
contador=0
for c in range(1,500):
    if c % 2 == 1 and c % 3 == 0:
     contador+=1
     s+=c
print(f'A soma dos {contador} valores solicitados é {s}')