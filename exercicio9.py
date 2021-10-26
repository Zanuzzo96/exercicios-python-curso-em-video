n = int(input('Digite um número para ver sua tabuada: '))

print('-' * 12)

c = 1
for c in range(1, 11):
    print(f'{n} x {c:2} = {(n*c):3}')
    c += 1
print('-' * 12)
