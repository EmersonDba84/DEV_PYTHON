'''
EXERCÍCIO: SOMA E MÉDIA DE INTEIROS
Crie um programa que calcule a soma de 5 valores inteiro.
Cada valor a ser somado é digitado pelo usuário. Imprima a soma na tela. Após a soma, calcule também a média dos valores e mostre na tela.
'''

soma = 0
cont = 1
while(cont <= 5):
    x = int(input(f'Digite o {cont}º número:'))
    soma = soma + x
    cont = cont + 1
print(f'Somatorio {soma}')

media = soma / 5
print(f'Media Final: {media}')