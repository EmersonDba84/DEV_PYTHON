peso = float(input('Digite seu Peso: '))
altura = float(input('Digite Sua Altura: '))

imc = peso / (altura ** 2)
print('Seu IMC é: ', imc)
if (imc >= 30):
    print('Voçe está Obeso!!')
elif(imc <= 30):
    print('Seu Indice de massa Corporal está na media')
else:
    print('Seu IMC é: ', imc)
