def fatorial(x=1,show=False):
    """
    --->Função que calcula o fatorial de um número, podendo mostrar ou não seu processo de calculo
    :param x:  Número que terá seu fatorial calculado
    :param show:(OPCIONAL) mostra ou não a conta. Utilize show False/True para alterar
    :return:Fatorial do número x
    """

    f = 1
    for c in range(x,0,-1):
        if show==True:
            print(f'{c}',end='')
            if c > 1:
                print(' X ',end='')
            else:
                print(' = ', end='')
        f *=c
    return f

print(fatorial(6,show=True))

