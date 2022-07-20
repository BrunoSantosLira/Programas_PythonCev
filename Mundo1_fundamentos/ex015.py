dias= float(input('Quantos dias alugados?'))
km= float(input('Quantos km pecorridos? '))
preçoP= dias * 60
preçokm= km * 0.15
print(f'O total a pagar é de: R${preçoP + preçokm:.2f}')