tabela= ('Corinthians','Atlético-MG','Santos','Avaí',
         'América-MG', 'Palmeiras','Bragantino','Internacional',
         'São Paulo', 'Botafogo','Fluminense','Coritiba','Cuiabá',
         'Athlético-PR','Flamengo','Goiás','Ceará-SC','Juventude',
         'Atlético-GO','Fortaleza')
print('-=-'*12)
print('Times Do Brasileirão')
print(tabela)
print('-=-'*12)
print('Os 5 primeiros colocados: ')
print(tabela[0:5])
print('-=-'*12)
print('Os 4 últimos colocados:')
print(tabela[-4:])
print('-=-'*12)
print('Times em ordem alfabética')
print(sorted(tabela))
print('-=-'*12)
posição= tabela.index('São Paulo')
print(f'O Flamengo está na {posição+1}² posição ')