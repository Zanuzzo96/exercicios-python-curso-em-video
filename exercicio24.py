palavra = str(input('Digite o nome da cidade: ')).strip()

print('{}'.format('SANTO' in palavra[:5].upper()))

''' 
    Formato feito pelo professor Guanabara 
    o enunciado dizia no inicio se começa com a palavra santo 
    então a forma que eu fiz a cima esta incorreta, pois esta verificando
    se tem na palavra toda a palavra santo
'''

print('{}'.format(palavra[:5].upper() == 'SANTO'))