'''
EXERCÍCIO 9: PAGANDO NO CARTÃO
Uma loja de departamentos está oferecendo diferentes formas de pagamento, conforme opções listadas a seguir.
Faça um algoritmo que leia o valor total de uma compra e calcule o valor do pagamento final de acordo com a opção escolhida.
Se a escolha for por pagamento parcelado, calcule também o valor de cada parcela. Ao final, apresente o valor total da compra e o valor das parcelas:

Pagamento à vista – conceder desconto de 5%;
Pagamento em 3x – o valor não sofre alterações;
Pagamento em 5x – acréscimo de 2%;
Pagamento em 10x – acréscimo 8%;
'''

print('PAGAMENTO')
print('1 - A vista')
print('2 - Parcelamento em 3x')
print('3 - Parcelamento em 5x')
print('4 - Parcelamento em 10x')
print('Digite outra tecla para sair....')

op = int(input('Qual a forma de pagamento deseja fazer'))
valor =  float(input('Qual o Preço do Produto?'))

if (op == 1):
    valor_final = valor * 0.95
    print(f'Produto comprado á vista. Total a pagar: {valor_final:.2f}.')
elif (op == 2):
    valor_final = valor
    parcela = valor_final / 3
    print(f'Produto Parcelado em 3x. Total a pagar: {valor_final}. valor da parcela: {parcela:.2f}.')
elif(op == 3):
    valor_final = valor * 1.02
    parcela = valor_final / 5
    print(f'Produto parcelado em 5x. Total a pagar: {valor_final}. valor da parcela: {parcela:.2f}.')
elif (op == 4):
    valor_final = valor * 1.08
    parcela = valor_final / 10
    print(f'Produto parcelado em 10x. total a pagar: {valor_final}. valor da parcela: {parcela:.2f}')
else:
    print('Opção Inválida.')
