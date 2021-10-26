dias = int(input('Quantos dias foi alugado: '))
kms = float(input('Quantos KMs Rodados: '))

valorAPagar = (dias * 60) + (kms * 0.15)
print('Valor a pagar pela locação é de R${:.2f}'.format(valorAPagar))