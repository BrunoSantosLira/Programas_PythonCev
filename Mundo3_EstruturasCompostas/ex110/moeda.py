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

def moeda(n=0, moeda='R$', sit=True):
    if sit == True:
        return f'{moeda} {n:.2f}'.replace('.',',')
    else:
        print(n)
        return n


def resumo(n,aumento=15,redução=15):
    print('-='*15)
    print(f'RESUMO DO VALOR'.center(30))
    print('-='*15)
    print(f'Preço Analisado: \t{moeda(n)}')
    print(f'Dobro Do Preço: \t{dobro(n,True)}')
    print(f'Metade Do Preço: \t{metade(n,True)}')
    print(f'{aumento}% De Aumento: \t{aumentando(n,aumento,True)}')
    print(f'{redução}% De Redução: \t{reduzindo(n,redução,True)}')
    print('-='*15)





