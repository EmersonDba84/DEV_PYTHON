#EXERCÍCIO 2
#Desenvolva um algoritmo que solicite ao usuário uma quantidade de dias, de horas, de minutos e de segundos.
#Calcule o total de segundos resultante e imprima na tela para o usuário.


d = int(input('Quantos dias'))
h = int(input('Quantas horas'))
m = int(input('Quantos minutos'))
s = int(input('Quantos segundos'))

total = s + (m * 60) + (h * 60 * 60) + (d * 24 * 60 *60)

res = f'O total de segundos calculado é de: {total}.'

print(res)



