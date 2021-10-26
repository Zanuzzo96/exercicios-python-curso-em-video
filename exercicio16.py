import math
from math import trunc

number = float(input('Digite um valor: '))

print(f'O valor digitado foi {number} e a sua porção inteira é {int(number)}')
print(f'O valor digitado foi {number} e a sua porção inteira é {math.trunc(number)}')
print(f'O valor digitado foi {number} e a sua porção inteira é {trunc(number)}')
