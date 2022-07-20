preço= float( input('Digite o preço do produto: R$'))
desconto= float( input('Digite o desconto que deseja calcular'))
multi= preço / 100 * (100 - desconto)
print(f'O produto que custava R${preço}, na promoção de {desconto}% irá custar R${multi:.2f}')