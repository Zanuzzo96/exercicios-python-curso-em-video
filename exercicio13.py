salario = float(input('Qual o salário do funcionário? R$'))
reajustado = salario + (salario * 15 / 100)

print(f'O salário de R${salario} reajustado fica R${reajustado:.2f}')
