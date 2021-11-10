distancia = float(input('Digite a distância do seu embarque ao seu destino em km: '))

if distancia <= 200:
    passagem = distancia * 0.5
else:
    passagem = distancia * 0.45
print(f'O valor da sua passagem é R${passagem:.2f}')

'''Formato simplificado que o professor mostrou na aula'''
preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'O preço da sua passagem é R${preco:.2f}')
