#DESAFIO
#Desenvolva um algoritmo para calcular o tempo de redução de vida de um fumante.
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou.
# Considere que o fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá, Exiba o total em dias.

qtd_dia = int(input('Quantos cigarros você fuma por dia?'))
anos_fumando = int(input('Você fuma/fumou por quantos anos?'))
dias_fumando = anos_fumando * 365

tempo_1cigarro = 10
total_cigarros = dias_fumando * qtd_dia

tempo_perdido_min = tempo_1cigarro * total_cigarros
tempo_perdido_dias = tempo_perdido_min / 60 / 24

print(f'Você fuma por {dias_fumando} dias. Um total de {total_cigarros} cigarros.')
print(f'O seu total de tempo de vida perdido, considerando que cada cigarro consome {tempo_1cigarro} minutos de sua vida é de {tempo_perdido_dias}.')