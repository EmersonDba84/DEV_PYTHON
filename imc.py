print(input('Qual Seu Nome?'))
print(input('Qual Sua idade?'))
peso = float(input('Digite seu Peso: '))
altura = float(input('Digite Sua Altura: '))

imc = peso / (altura ** 2)
print('Seu IMC é: ', imc)
if (imc >= 30):
    print('Você está Obeso!!')
elif(imc <= 30):
    print('Seu Índice de massa Corporal está na media')
else:
    print('Seu IMC é: ', imc)