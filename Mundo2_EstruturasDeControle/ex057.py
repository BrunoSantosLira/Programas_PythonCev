sexo=''
while sexo != 'M' and  sexo != 'F':
      sexo= input(' Digite o seu sexo [M/F]:').upper().strip()
      if sexo != 'M' and sexo != 'F':
         print('SEXO INVÁLIDO!!! Por favor, ',end='')
      else:
          print(f'SEXO {sexo} REGISTRADO COM SUCESSO!')