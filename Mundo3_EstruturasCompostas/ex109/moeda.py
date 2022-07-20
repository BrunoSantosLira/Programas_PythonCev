def metade(n,sit=True):
    n /= 2
    if sit== True:
        return moeda(n)
    else:
        return n


def dobro(n,sit= True):
    n *= 2
    if sit== True:
        return moeda(n)
    else:
        return n


def aumentando(n,aumento,sit= True):
    todo= 100 + aumento
    n = (n / 100) * todo
    if sit == True:
        return moeda(n)
    else:
        return n

def reduzindo(n,redução, sit= True):
    todo= 100 - redução
    n = (n / 100) * todo
    if sit == True:
        return moeda(n)
    else:
        return n

def moeda(n=0, moeda='R%', sit=True):
    if sit == True:
        return f'{moeda} {n:.2f}'.replace('.',',')
    else:
        print(n)
        return n



