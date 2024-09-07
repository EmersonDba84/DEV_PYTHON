'''
EXERCÍCIO: CONTAGEM REGRESSIVA
Faça um programa em Python para exibir na tela uma contagem regressiva do lançamento de um foguete, iniciando em 10 até 0, e escrevendo após o 0, a palavra: Fogo!
'''

contador = 10
while(contador >= 10):
    print(contador)
    contador = contador - 1
print('Fogo!')