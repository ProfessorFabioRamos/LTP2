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
    
inserir_cliente('Joao',45,'joao@email.com',data_hora_local)
inserir_cliente('Helena',16,'helena@email.com',data_hora_local)
inserir_cliente('Renata',16,'renata@email.com',data_hora_local)
inserir_cliente('Pedro',45,'pedro@email.com',data_hora_local)
inserir_cliente('Manuel',30,'manuel@email.com',data_hora_local)
inserir_cliente('Carla',41,'carla@email.com',data_hora_local)

#cursor.execute("SELECT * FROM clientes") # SELECIONA TODOS OS REGISTROS
#cursor.execute("SELECT nome, date_time_conta FROM clientes") #APENAS COLUNAS ESPECIFICAS
#cursor.execute("SELECT * FROM clientes ORDER BY idade ASC") # ORDENA RESULTADOS (DESC-decrescente)
#cursor.execute("SELECT * FROM clientes WHERE idade > 30") # FILTRO DE RESULTADOS
#cursor.execute("SELECT * FROM clientes WHERE idade > 30 AND email LIKE '%@email.com'") # FILTRO DE RESULTADOS
#cursor.execute("SELECT * FROM clientes LIMIT 1") #LIMITANDO OS RESULTADOS
#cursor.execute("SELECT * FROM clientes ORDER BY idade ASC LIMIT 1") #LIMITANDO OS RESULTADOS POR ORDEM
cursor.execute("SELECT idade, COUNT(*) FROM clientes GROUP BY idade") #AGRUPANDO RESULTADOS

resultados_1 = cursor.fetchall()
for c in resultados_1:
    print(c)

conexao.commit()
conexao.close()