#EXERCÍCIO 5
#Desenvolva um algoritmo que seja capaz de calcular a soma e a subtração entre 2 valores com vírgula.
# Crie duas variáveis de teste. Uma que testa se a soma é maior do que 10. Outra que testa se a subtração é menor do que 0.
# Imprima tudo na tela.

x = float(input('Digite um numero inteiro:'))
y = float(input('Digite outro numero inteiro:'))

soma = x + y
sub = x - y
testeA = soma > 10
testeB = sub < 10

print(f'Soma: {soma:.2f}. Subtração {sub:.1}.')
print(f'A Soma é maoir que 10? {testeA}')
print(f'A Subtração é menor do que 0?: {testeB}')


'''
#versão do módulo 2
x = float(input('Digite um valor:'))
y = float(input('Digite um segundo valor:'))

soma = x + y
sub  = x - y
print(f'Soma: {soma:.2f}. Subtração: {sub:.2f}')

if (soma > 10):
    print('A soma é maior do que 10.')
if (sub < 0):
    print('A subtração é menor do que 0.')
'''
