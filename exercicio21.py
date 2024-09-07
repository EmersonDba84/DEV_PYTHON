'''
EXERCÍCIO: INTERVALO DE PARES DELIMITADO PELO USUÁRIO
Suponhamos que desejamos exibir uma série de números na tela, onde os limites de início e fim dessa sequência são determinados pelo usuário que executa o programa.
Crie um algoritmo que leia os valores de ínício e de fim de novo programa, e imprima na tela o intervalo de número pares correspondentes.
'''

inicial = int(input('Qual o Valor deseja iniciar a contagem?'))
final = int(input('Qual Valor deseja finalizar a contagem?'))
i = inicial
while(i <= final):
    if(i% 2 == 0):
        print(i)
    i = i - 1