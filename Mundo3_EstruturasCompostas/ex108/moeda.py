def metade(n):
    n /= 2
    return n


def dobro(n):
    n *= 2
    return n


def aumentando(n,aumento):
    todo= 100 + aumento
    n = (n / 100) * todo
    return n

def reduzindo(n,redução):
    todo= 100 - redução
    n = (n / 100) * todo
    return n


def moeda(preço=0, moeda='R%'):
    return f'{moeda} {preço:.2f}'.replace('.',',')
