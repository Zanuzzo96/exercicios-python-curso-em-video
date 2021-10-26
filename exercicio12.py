preco = float(input('Qual é o preço do produto? R$'))

print(f'O produto que custava R${preco}, na promoção com desconto de 5% vai custa R${(preco - (preco * 5 / 100)):.2f}')
