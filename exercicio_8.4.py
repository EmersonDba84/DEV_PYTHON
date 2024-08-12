'''
EXPRESSÕES LÓGICAS/BOOLEANOS
Depois de explorar os operadores lógicos, vamos entender como mesclá-los em expressões, incluindo a adição de operadores relacionais e aritméticos.

Antes, porém, é fundamental conhecer a ordem de precedência quando estas operações são processadas pelo Python. Como em muitas linguagens de programação,
o Python possui uma sequência específica na qual executa cada operação.

Para as operações aritméticas, a sequência é similar ao que aprendemos na matemática elementar.
Por exemplo, multiplicação e divisão vêm antes de soma e subtração. Mas também temos que considerar os operadores relacionais e lógicos. A sequência de execução é:

Parênteses;
Operadores aritméticos de potenciação e radiciação;
Operadores aritméticos de multiplicação, divisão e módulo;
Operadores aritméticos de soma e subtração;
Operadores relacionais;
Operador lógico "not";
Operador lógico "and";
Operador lógico "or";
Atribuições.
Operações que possuem a mesma prioridade são processadas da esquerda para a direita. Por exemplo, em uma expressão com duas somas, a da esquerda é realizada primeiro.
'''

a = 5
b = 20
result = not a < b
print(result)

a = 15
b = 2
c = 7.5
result = (a < b) or (c > b)
print(result)

x = 10
y = 1
z = 5.5
res = x > y or not z == y and y != y + z / x
print(res)