'''
EXERCÍCIO 1: IDADE PARA DIRIGIR
Desenvolva um algoritmo que solicite o seu ano de nascimento e o ano atual. Calcule a sua idade e apresente na tela.
 Para fins de simplificação, despreze o dia e o mês do ano. Após o cálculo,
verifique se a idade é maior ou igual a 18 anos e apresente na tela uma mensagem informando que já é possível tirar a carteira de motorista caso seja de maior.
'''

ano_nascimento = int(input('Qual seu ano de nascimento?'))
ano_atual = int(input('Em que ano estamos?'))
idade = ano_atual - ano_nascimento

print(f'Você tem {idade} anos de idade.')
if(idade >= 18):
    print('Você é de maior. Já pode tirar a carteira de motorista.')