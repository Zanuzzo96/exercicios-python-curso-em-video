import math
from math import sqrt

#sem a biblioteca nenhuma importada
n = int(input('Digite um número:'))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)

print('O dobro de {} vale {}'.format(n, dobro))
print('O triplo de {} vale {}'.format(n, triplo))
print('A raiz quadrada (arredondada) de {} é igual a {:.2f}'.format(n, raiz))
print('A raiz quadrada (exata) de {} é igual a {}'.format(n, raiz))
print('A raiz quadrada de {} é igual a {}'.format(n, pow(n, (1/2    ))))

#com a biblioteca math importada

raiz2 = math.sqrt(n)
print('A raiz quadrada "exata" com a biblioteca de {} é igual {}'.format(n, raiz2))
print('A raiz quadrada "arredondada" com a bilbioteca de {} é igual {:.2f}'.format(n, raiz2))
print(f'a raiz quadrada "arredondada" com a biblioteca e fstring de {n} é igual {raiz2:.2f}')

#importando somente o metodo para calcular a raiz da biblioteca Math

raiz3 = sqrt(n)
print('A raiz quadrada de {} usando somente o metodo sqrt da biblioteca math é {}'.format(n, raiz3))
print(f'A raiz quadrada de {n} usando somente o metodo sqrt da biblioteca math e fstring é {raiz3}')
print(f'A raiz quadrada "arredondada" de {n} usando somente o metodo sqrt da bibliote math e fstring é {raiz3:.2f}')