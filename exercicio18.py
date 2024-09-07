'''
CONDICIONAL COMPOSTA (IF-ELSE)
A estrutura condicional composta existe para quando precisamos decidir se um conjunto de instruções A precisa ser executado, ou se será outro conjunto de instruções B a ser executado.
Note que nunca acontecerá de ambos conjuntos de instruções serem executadas em um mesmo fluxo de execução do algoritmo. Será sempre um, ou outro. Nunca ambos.
Não obstante, o conjunto A e o conjunto B podem conter instruções completamente distintas entre si.
Podendo inclusive apresentar uma quantidade de instruções bastante diferentes também. Não existem restrições quanto a

if ():
    # Instrução (ões) A
else:
    # Instrução (ões) B
'''

#Lê dois valores inteiros e compara ambos
x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um segundo valor inteiro: '))
if (x > y):
  print('O primeiro valor é maior que o segundo!')
else:
  print('O segundo valor é maior que o primeiro!')

# Lê dois valores inteiros e compara ambos
x = int(input('Digite um valor inteiro: '))
y = int(input('Digite um segundo valor inteiro: '))

if x > y:
    print('O primeiro valor é maior que o segundo!')
elif x < y:
    print('O segundo valor é maior que o primeiro!')
else:
    print('Os dois valores são iguais!')
