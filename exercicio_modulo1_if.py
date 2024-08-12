#MÓDULO 2
#ESTRUTURAS CONDICIONAIS

#versão do módulo 1
'''x = float(input('Digite um valor:'))
y = float(input('Digite um segundo valor:'))

soma = x + y
sub  = x - y
testeA = soma > 10
testeB = sub < 0

print(f'Soma: {soma:.2f}. Subtração: {sub:.2f}')
print(f'A soma é maior do que 10? {testeA}')
print(f'A subtração é menor  do que 0? {testeB}')'''


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