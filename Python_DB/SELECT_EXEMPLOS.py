import sqlite3
from datetime import datetime
import pytz

fuso = pytz.timezone('America/Sao_Paulo')
data_hora_local = datetime.now(fuso).strftime('%Y-%m-%d %H:%M:%S')
print(data_hora_local)

conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    email TEXT,
    date_time_conta TIMESTAMP
)
""")

def inserir_cliente(n,i,e,d):
    cursor.execute("INSERT INTO clientes (nome,idade,email,date_time_conta) VALUES(?,?,?,?)",
        (n,i,e,d))
    
# inserir_cliente('Kyle', 16, 'kyle@gmail.com', data_hora_local)
# inserir_cliente('Helena', 16, 'helena@hotmail.com', data_hora_local)
# inserir_cliente('Manuel', 45, 'manuel@gmail.com', data_hora_local)
# inserir_cliente('Cartman', 23, 'cartman@gmail.com', data_hora_local)
# inserir_cliente('Alice', 45, 'alice@email.com', data_hora_local)
# inserir_cliente('Jenny', 34, 'jenny@email.com', data_hora_local)

#cursor.execute("SELECT * FROM clientes") # SELECIONA TODOS OS REGISTROS
#cursor.execute("SELECT nome, idade FROM clientes") #APENAS COLUNAS ESPECIFICAS
#cursor.execute("SELECT * FROM clientes ORDER BY idade ASC") # ORDENA RESULTADOS (DESC-decrescente)
#cursor.execute("SELECT * FROM clientes ORDER BY nome DESC") # ORDENA RESULTADOS (DESC-decrescente)
#cursor.execute("SELECT * FROM clientes WHERE idade > 30") # FILTRO DE RESULTADOS
#cursor.execute("SELECT * FROM clientes WHERE email LIKE '%@gmail.com'") # FILTRO DE RESULTADOS COM FINAL ESPECIFICO
#cursor.execute("SELECT * FROM clientes WHERE idade > 18 AND email LIKE '%@gmail.com'") # FILTRO DE RESULTADOS COM FINAL ESPECIFICO
#cursor.execute("SELECT * FROM clientes LIMIT 2") #LIMITANDO OS RESULTADOS
#cursor.execute("SELECT * FROM clientes ORDER BY idade ASC LIMIT 1") #LIMITANDO OS RESULTADOS POR ORDEM
cursor.execute("SELECT idade, COUNT(*) FROM clientes GROUP BY idade") #AGRUPANDO RESULTADOS

resultados_1 = cursor.fetchall()
for c in resultados_1:
    print(c)

conexao.commit()
conexao.close()
