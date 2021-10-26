import math
angulo = float(input('Digite o ângulo que você deseja: '))

seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))

print(f'Seno de {angulo}° é {seno:.2f}')
print(f'Cosseno de {angulo}° é {cosseno:.2f}')
print(f'Tangente de {angulo}° é {tangente:.2f}')
