def maior(* num):
    print('-='*15)
    print('ANALISANDO...')
    for c in num:
        print(f'{c}...',end=' ')
    print(f'Foram analisados {len(num)} valores ao todo ',end=' ')
    print(f'\nO maior valor é {max(num)} ')

maior(3,4,5,2,9,4)
maior(2,1,5)
maior(0,5)
maior(9)
maior(0)