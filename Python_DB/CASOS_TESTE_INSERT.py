import sqlite3

conexao = sqlite3.connect("Inventario.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS itens(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE NOT NULL,
    tipo TEXT NOT NULL,
    valor INTEGER CHECK (valor > 0)
    )
""")

# CREATE - Inserir item
def inserir_item(nome,tipo,valor):
    # VALIDAÇÕES
    if not isinstance(nome,str):
        print('Name com tipo incorreto!')
        return
    if not isinstance(valor,int):
        print('Valor com tipo incorreto!')
        return 
    
    try:
        cursor.execute("INSERT INTO itens (nome,tipo,valor) VALUES(?,?,?)", 
                       (nome,tipo,valor))
        conexao.commit()
        print("Item inserido com sucesso")
    except sqlite3.IntegrityError as e:
        print("Erro: ", e)

##################### CASOS DE TESTE DA FUNÇÃO INSERIR ##########################################

# #Teste comum e válido
# inserir_item('Espada Vorpal', 'Arma', 1000)
# # Teste com item já existente
# inserir_item('Espada Vorpal', 'Arma', 2000)
# # Teste com valor negativo
# inserir_item('Poção', 'Cura', -100)
# # Teste com tipo incorreto
# inserir_item(6000, 'Arma', 1000)
# # Teste com tipo incorreto
# inserir_item('Escudo de Ferro', 'Arma', '1000')

conexao.close()
