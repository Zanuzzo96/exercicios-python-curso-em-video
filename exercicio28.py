from random import randint

print("Vou pensar num número entre 0 e 5. Tente adivinhar ....")
numeroPensado = randint(0,5)
numeroDigitado = int(input('Em que número eu pensei?'))

if numeroPensado == numeroDigitado:
    print('PARABÉNS! Você acertou miseravi')
else:
    print(f'Você errou, eu pensei no número {numeroPensado} e não no {numeroDigitado}')
