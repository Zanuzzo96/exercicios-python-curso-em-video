tempo = True
mensagem = 'carro novo' if tempo <= 3 else 'carro velho'

print(mensagem)

print('carro novo' if tempo <= 3 else 'carro velho')


tempoB = 5
if tempoB == 3 or tempo == False:
    print('é um três')
else:
    print('o numero não é 3')

# aula 11 condicoes

if tempoB == 3 or tempo == False:
    print('primeira validacao')
elif tempo == True or tempoB != 3:
    print('segundo bloco')
else:
    print('terceiro bloco')