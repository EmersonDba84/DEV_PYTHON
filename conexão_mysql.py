import mysql.connector

# Estabelecendo a conexão com o banco de dados
conn = mysql.connector.connect(
    host="localhost",       # Ou o endereço do seu servidor MySQL
    user="root",     # Substitua por seu usuário MySQL
    password="",   # Substitua pela sua senha MySQL
    database="radiadores_setembro_2024"  # Nome do banco de dados que você quer acessar
)

cursor = conn.cursor()

# Exemplo de dados a serem inseridos
nome = "João"
idade = 25

# Inserindo os dados na tabela
sql = "INSERT INTO entrada (nome, idade) VALUES (%s, %s)"
val = (nome, idade)

cursor.execute(sql, val)

# Confirmando a inserção
conn.commit()

print(cursor.rowcount, "registro(s) inserido(s) com sucesso.")

# Fechar a conexão
cursor.close()
conn.close()
