'''
EXERCÍCIO 2: BONIFICAÇÃO AO FUNCIONÁRIO
Uma empresa concedeu um bônus de 20% para todos seus funcionários com mais de 5 anos de empresa.
Todos os outros que não se enquadram nesta categoria receberam uma bonificação de 10%, somente.
Escreva um algoritmo que leia o salário do funcionário e seu tempo de empresa, e apresente a bonificação de cada funcionário na tela.
'''

salario = float(input('Qual é seu salario'))
ano_admissao = int(input('Digite o Ano que foi contratado'))
ano_atual = float(input('Em que ano estamos?'))

tempo = ano_atual - ano_admissao
if(tempo > 5):
    bonus = salario * 0.2
else:
    bonus = salario * 0.1

print(f'voçe tem {tempo} anos de empresa.')
print(f'Seu salario é de  {salario} ')
print(f'E sua bonificação é bonus {bonus}')
print(f'Salario final: {salario + bonus}')