Largura = float(input('Largura da parede:'))
Altura = float(input('Altura da parede: '))

m2 = Largura*Altura

print(f'Sua parede tem a dimensão de {Largura} x {Altura} e sua área é de {m2}m².')
print(f'Para pintar essa parede, você precisará de {(m2/2)}l de tinta')
