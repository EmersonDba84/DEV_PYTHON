'''
CONDICIONAIS ANINHADAS
Os programas de computador frequentemente vão além da utilização de uma única estrutura condicional básica ou até mesmo composta.
É comum empregarmos múltiplas condicionais aninhadas em um algoritmo, implicando em uma estrutura dentro da outra.
Vale ressaltar que podemos ter quantas condicionais aninhadas desejarmos, não limitando-se a apenas duas.
No entanto, para simplificar o entendimento, nos atemos à representação de apenas duas neste contexto.
'''

#Lê dois valores inteiros e compara ambos
x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um segundo valor inteiro: '))
if (x > y):
  print('O primeiro valor é maior que o segundo!')
else:
    if (x < y):
        print('O segundo valor é maior que o primeiro!')
    else:
        print('Ambos números são iguais!')