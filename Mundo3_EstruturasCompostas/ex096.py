def área(largura,comprimento):
    a= largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é {a}m²')

print('CONTROLE DE TERRENOS')
print('-'*20)
largura= float(input('LARGURA(m):'))
comprimento= float(input('COMPRIMENTO(m):'))


área(largura, comprimento)