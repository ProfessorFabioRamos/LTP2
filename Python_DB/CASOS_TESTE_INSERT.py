# Casos de Teste
import sqlite3

conexao = sqlite3.connect('empresa.db')
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS itens(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE NOT NULL,
    tipo TEXT NOT NULL,
    valor INTEGER CHECK (valor > 0)
    )
""")

def inserir_itens(nome, tipo,valor):
    # VALIDAÇÕES
    #print(type(nome))
    #VALIDAÇÃO DE STRING
    if not isinstance(nome, str):
        print("Name com tipo incorreto")
        return
    #VALIDAÇÃO DE INTEIRO
    if not isinstance(valor, int):
        print("Valor com tipo incorreto")
        return
    try:
        cursor.execute("INSERT INTO itens(nome, tipo,valor) VALUES(?,?,?)",
                    (nome, tipo,valor))
        conexao.commit()
        print("Item inserido com sucesso!")
    except sqlite3.IntegrityError as e:
        print("Erro:",e)

##################### CASOS DE TESTE DA FUNÇÃO INSERIR ###########################
#TESTE POSITIVO
inserir_itens("Espada de Aço","Arma",500)
# TESTE NEGATIVO COM ITEM JÁ EXISTENTE
inserir_itens("Espada de Aço","Arma",500)
# TESTE NEGATIVO COM VALOR NÃO PERMITIDO
inserir_itens("Espada de Ouro","Arma",-800)
# TESTE NEGATIVO COM TIPO INCORRETO (INT)
inserir_itens(5000,"Arma",800)
# TESTE NEGATIVO COM TIPO INCORRETO (STR)
inserir_itens("Poção Menor","Cura",'20')

conexao.close()
