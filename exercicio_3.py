#EXERCÍCIO 3
#Desenvolva um algoritmo que solicite ao usuário o preço de um produto e um percentual de desconto a ser aplicado a ele.
# Calcule e exiba o valor do desconto e o preço final do produto.

preco = float(input('Digite o Preço do Produto'))
p = float(input('Digite o percentual de desconto (0 -100%)'))

desconto = preco * (p/100)
final = preco - desconto
print(f'O preço do produto é {preco}. Desconto aplicado de {p}%.')
print(f'O valor do desconto calculado: {desconto}.')
print(f'Valor Final do Produto: {final}.')

