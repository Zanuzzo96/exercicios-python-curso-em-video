''' nome = str(input('Digite seu nome completo: '))

print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minuscula é {}'.format(nome.lower()))

particaoNome = nome.split()
countLetrasNome = ''.join(particaoNome)

print('Seu nome tem ao todo {} letras'.format(len(countLetrasNome)))
print('Seu primeiro nome é {} e ele tem {} letras'.format(particaoNome[0], len(particaoNome[0]))) '''

''' Como foi feito pelo professor Guanabara '''

nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculo é {}'.format(nome.upper()))
print('Seu nome em minuscula é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
primeiroNome = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(primeiroNome[0], nome.find(' ')))

