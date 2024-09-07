'''
DESAFIO
Faça um algoritmo que receba três valores, representando os lados de um triângulo fornecidos pelo usuário.
Verifique se os valores formam um triângulo e classifique como:
Equilátero (três lados iguais);
Isósceles (dois lados iguais quaisquer);
Escaleno (três lados diferentes).
Lembre-se de que, para formar um triangulo, nenhum dos lados pode ser igual a zero e um lado não pode ser maior do que a soma dos outros dois.
'''

A = int(input('Digite o 1º Lado do triângulo:'))
B = int(input('Digite o 2º Lado do Triângulo:'))
C = int(input('Digite o 3º Lado do Triângulo:'))

if A > 0 and B > 0 and C > 0:
    if A + B > C and A + C > B and B + C > A:
        if A != B and A != C and B!= C:
            print('Triângulo escaleno.')
        else:
            if A == B and A == C and B == C:
                print('Triângulo equilátero.')
            else:
                print('Triângulo isósceles.')

    else:
        print('Ao menos um dod valores indicados não servem para formar um triângulo')
else:
    print('Ao menos um dos valores indicados não servem para formar um triângulo.')
