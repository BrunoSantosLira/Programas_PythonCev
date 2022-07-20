with open('teste.txt', 'a+', encoding = "utf-8") as file:
        nome= str(input('Digite um nome:'))
        idade= int(input('Idade:'))
        file.write(f'{nome:}')
        file.write(f'{idade:>30} \n')
        file.seek(0)
        print(file.read())