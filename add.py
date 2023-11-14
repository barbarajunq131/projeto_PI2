import sqlite3

# Conectar ao banco de dados (se não existir, ele será criado)
conn = sqlite3.connect('ongs.db')
c = conn.cursor()

# Criar a tabela "ongs" (se ainda não existir)
c.execute('''
    CREATE TABLE IF NOT EXISTS ongs (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        endereco TEXT,
        CEP TEXT,
        area_atuacao TEXT
    )
''')
# Dados fictícios para a base de dados (simulação)
ongs = [
    ("ONG A", "Endereço A", "12345-678", "Meio Ambiente"),
    ("ONG B", "Endereço B", "54321-876", "Saúde"),
    ("ONG C", "Endereço C", "98765-432", "Educação"),
    ("ONG D", "Endereço D", "24680-135", "Meio Ambiente"),
]

# Adicionar a coluna 'area_atuacao' se não existir
try:
    c.execute("ALTER TABLE ongs ADD COLUMN area_atuacao TEXT")
    conn.commit()
except sqlite3.OperationalError as e:
    pass

conn.close()

print("Banco de dados criado com sucesso.")

