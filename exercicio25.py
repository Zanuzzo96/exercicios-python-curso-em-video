nome = str(input("Qual é o seu nome completo? "))
print(f'Seu nome tem tem Silva? {"silva" in nome.lower()}')

'''Abaixo é um teste de contador de palavra dentro da string
    Não tem nada haver com o exercicio foi um extra meu'''
print(f'Tem {nome.lower().count("silva")} Silva no nome')

