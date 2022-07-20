import math
angulo= float( input('Digite o ângulo que você deseja:'))
seno= math.sin(math.radians(angulo))
cosseno= math.cos(math.radians(angulo))
tangente= math.tan(math.radians(angulo))
print(f'O ângulo de {angulo} possuí seno de {seno:.2f}')
print(f'O ângulo de {angulo} possuí cosseno de {cosseno:.2f}')
print(f'O angulo de {angulo} possuí tangente de {tangente:.2f}')
