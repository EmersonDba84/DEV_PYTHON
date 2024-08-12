'''
O exemplo que vamos resolver agora descobre se um número inteiro digitado é par ou é ímpar. Para resolvermos este exercício,
devemos pensar em que teste lógico deve ser feito para descobrirmos se um numero é par ou ímpar.
Se pegarmos qualquer valor numérico e inteiro e dividirmos por 2, que é par, e esta divisão resultar em resto zero,
sabemos que o número digitado é divisível por 2, e portanto, é par . Caso o resto desta divisão não dê zero, significa que o número não é divisível por 2, e portanto, é ímpar.
Na linguagem Python, podemos obter o resto de uma divisão diretamente utilizando o símbolo de percentual .
Deste modo, podemos escrever a expressão lógica x % 2==0. Ou seja, obtemos o resto da divisão por 2 e, em seguida, pela comparação lógica de igualdade verificamos se é igual a zero.
Ademais, a ordem de precedência dos operadores também deve ser respeitada aqui.
Primeiro, o cálculo aritmético é realizado e por último o teste lógico. Ficamos com o algoritmo a seguir.
'''

x = int(input('Digite um valor inteiro'))
if(x % 2 == 0):
    print('O número é par!')
else:
    print('O número é impar!')