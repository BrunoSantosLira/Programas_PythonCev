def leiaDinheiro(dinheiro):
    while True:
        dinheiro=  input('Digite um preço:')
        dinheiro = dinheiro.replace(',','.')
        print(dinheiro.isdecimal())
        if dinheiro.isnumeric() == False:
            print(f'\033[31m ERRO! "{dinheiro}" não é valor monetário válido\033[m')
        else:
            return float(dinheiro)