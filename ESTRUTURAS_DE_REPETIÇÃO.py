'''
A IMPORTÂNCIA DAS ESTRUTURAS DE REPETIÇÃO
Observe que o comando de movimentação aparece cinco vezes no algoritmo.
É comum ter repetições de instruções em um programa. De fato, repetir o comando de movimento algumas vezes não parece ser tão cansativo, não é?

Agora, imagine se, em vez de se deslocar cinco espaços até a praia, você tivesse que avançar 100 quadradinhos.
Executar o movimento 100 vezes no algoritmo seria extremamente trabalhoso (e nem vamos tentar fazer isso neste material).
E se fosse mil vezes ou até um milhão? Você repetiria o mesmo comando todas essas vezes? Claro que não, pois além de ser exaustivo, deixaria seu programa longo e confuso.

Por isso, linguagens de programação possuem estruturas de repetição.
Com elas, podemos criar um segmento no programa onde todas as instruções são repetidamente executadas até que determinada condição seja atendida,
encerrando o que denominamos de loop (ou ciclo) de repetição.

Vamos explorar outro exemplo, desta vez em Python, para ilustrar a importância de um ciclo de repetição.
Suponhamos que queiramos exibir na tela uma sequência de números de 1 a 5 em ordem ascendente. Poderíamos fazer isso com simples comandos print para cada número.


print(1)
print(2)
print(3)
print(4)
print(5)

Também podemos abordar o mesmo problema utilizando uma variável x, que muda seu valor a cada execução do comando print. Veja:

x = 1
print(x)
x = 2
print(x)
x = 3
print(x)
x = 4
print(x)
x = 5
print(x)

Se adotarmos qualquer uma das abordagens mencionadas anteriormente, teríamos que modificar o valor da variável (ou do print) a cada nova impressão.
Pense se quiséssemos imprimir até o número 100 ou 1000; elaborar o código manualmente seria extremamente tedioso.

Podemos otimizar esse processo com a abordagem a seguir: começamos com x igual a um e simplesmente vamos adicionando (incrementando) a cada etapa.
Dessa forma, não há necessidade de ajustar o valor de x manualmente para cada impressão.

x = 1
print(x)
x = 2
print(x)
x = 3
print(x)
x = 4
print(x)
x = 5
print(x)

x = 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)
x = x + 1
print(x)

ESTRUTURA DE REPETIÇÃO: WHILE
Começaremos nossos estudos sobre laços de repetição com a estrutura conhecida como "enquanto".
Em Python, essa estrutura é denominada "while". Ela repete um conjunto de instruções enquanto uma certa condição permanecer verdadeira.
Se a condição não for atendida, o programa avança para a primeira linha de código após esse laço. A Figura ilustra a representação do "while" por meio de um fluxograma.

Note que todas as instruções devem estar corretamente indentadas para serem associadas ao bloco de loop.
Lembre-se, ao contrário de linguagens como Java e C/C++ que possuem delimitadores, Python usa a indentação para determinar a extensão do bloco,
eliminando a necessidade de um finalizador específico.

Retornando ao exercício inicial desta aula, onde queríamos exibir os números de 1 a 5 em ordem ascendente. Isso pode ser alcançado usando o laço de repetição "while".
Vejamos como seria:

i = 1
while (i <= 5):
  print(i)
  i = i + 1

  i = 0
while (i < 100):
  print(i)
  i = i + 1
'''