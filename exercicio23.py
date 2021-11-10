numero = int(input('Informe um número: '))
numStr = str(numero)
'''

print(f'Analisando o número {numStr}')
print(f'Unidade: {numStr[3]}')
print(f'Dezena: {numStr[2]}')
print(f'Centena: {numStr[1]}')
print(f'Milhar: {numStr[0]}')

'''

''' Sem dar erro caso não seja inserido um numero de 4 digitos '''

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'Analisando o número {numero}')
print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar: {milhar}')
