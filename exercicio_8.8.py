'''A linguagem Python consegue usar a múltima escolha de maneira mais flexível. Podemos colocar diferentes condições nos elifs. Veja:'''

nome = input('Qual seu nome ?')
idade = int(input('Qual sua idade?'))

if nome == 'Emerson':
    print('Olá Emerson')
elif idade < 18:
    print('Voçe não é o Emerson!, e voçe é menor de idade.')
elif idade > 100:
    print('Diferente de voçe o Emerson não é imortal')