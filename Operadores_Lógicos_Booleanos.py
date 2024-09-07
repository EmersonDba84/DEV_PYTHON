'''
OPERADORES LÓGICOS/BOOLEANOS
Já discutimos os principais operadores aritméticos e relacionais no MÓDULO 1. Em breve, exploraremos como esses operadores podem ser usados em expressões lógicas.
No entanto, ainda precisamos abordar um terceiro tipo de operador: o operador lógico ou booleano.
Esses operadores são utilizados para agrupar operações e formar expressões lógicas, com características específicas.
Por padrão, o Python suporta três desses operadores, ainda que a álgebra de Boole contenha outros. São eles: o operador "and" (conjunção),
"or" (disjunção) e "not" (negação). No Python, esses operadores são escritos da mesma forma que são pronunciados em inglês.
Cada operador segue um conjunto de normas representadas pela sua respectiva tabela verdade.
Essa tabela exibe o resultado de uma ação envolvendo um ou dois valores lógicos.
O operador de negação atua sobre um único valor, tornando-o unitário, enquanto os operadores de conjunção e disjunção atuam sobre dois valores, sendo, portanto, binários.

OPERADOR NOT
Começaremos pelo operador mais básico.
O operador de negação "not" é utilizado para inverter um valor lógico ou o resultado de uma expressão booleana.
Isso indica que o resultado final da expressão será o oposto do original. A tabela verdade do "not" é mostrada abaixo, onde a coluna V indica um valor booleano.
No Python, o valor booleano verdadeiro é denotado pela palavra em inglês "True", enquanto o falso é representado por "False". Usaremos esses termos a partir de agora.

OPERADOR AND
O operador "and", que é binário, trabalha com dois valores, referidos como valores de entrada, e produz um valor como resultado.
Esse operador retornará verdadeiro apenas quando ambas as entradas também forem verdadeiras. A tabela verdade do "and" é exibida na Tabela, onde as colunas V1 e V2 denotam valores booleanos.
A tabela mostra todas as combinações binárias possíveis.

OPERADOR OR
O operador "or", de natureza binária, atua sobre dois valores que consideramos como valores de entrada, produzindo um valor de resultado.
Este operador retorna verdadeiro se pelo menos uma das entradas for verdadeira. A tabela verdade correspondente ao "or" é mostrada a seguir, onde as colunas V1 e V2 denotam valores booleanos.
A Tabela exibe todas as combinações binárias possíveis.
Realize os testes abaixo para todas as combinações possíveis da tabela verdade e veja se os resultados coincidem com ela.
'''

# or
a = False
b = False
print(a or b)

