from random import randint
num= (randint(0,9), randint(0,9),randint(0,9), randint(0,9), randint(0,9))
for c in num:
    print(c, end=' - ')
print(f'\n O maior valor foi: {max(num)}')
print(f' Enquanto o menor foi: {min(num)}')