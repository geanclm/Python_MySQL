# Conectando base de dados MySQL com Python
# by geanclm on 29/10/2023

# Primeira etapa realizada para instalar o conector de banco
# pip install mysql-connector-python

import mysql.connector

conexao = mysql.connector.connect (
    host = 'localhost',
    user = 'root',
    password = 's145',
    database = 'estudo_db',
)

cursor = conexao.cursor()

# CRUD


cursor.close()
conexao.close()