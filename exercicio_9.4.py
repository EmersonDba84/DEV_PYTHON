'''
EXERCÍCIO: TABUADA
Crie um programa que calcule a tabuada de um número escolhido pelo usuário. Imprima na tela a tabuada deste número de 1 a 10.
Ao realizar a impressão na tela, mostre os valores formatados conforme a seguir. Exemplo com a tabuada do 5: 1x5=5, 2x5=10, 3x5=15...
'''

num = int(input('Digite um numero para calcular a Tabuada:'))
i = 1
print(f'TABUADA DO {num}')
while (i <= 10):
    print(f'{i} x {num} = {i * num}')
    i = i + 1