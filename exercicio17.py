import math

catetoOposto = float(input('Comprimento do cateto oposto: '))
catetoAdjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusaMath = math.hypot(catetoOposto, catetoAdjacente)

hipotenusa = (catetoOposto ** 2 + catetoAdjacente ** 2) ** (1/2)

print(f'A hipotenusa vai medir {hipotenusa:.2f}')
print(f'A hipotenusa vai medir {hipotenusaMath:.2f}')
