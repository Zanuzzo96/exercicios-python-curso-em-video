velocidade = float(input('Qual a velocidade atual do veiculo? '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'Você está acima da velocidade permitida e foi multado no valor R$ {multa:.2f}')
else:
    print('Você esta dentro da velocidade permitida \nTenha um excelente dia')
