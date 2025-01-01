import sqlite3

# Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect('cars.db')
c = conn.cursor()

# Criar a tabela de carros
c.execute('''CREATE TABLE IF NOT EXISTS cars
             (id INTEGER PRIMARY KEY,
              model TEXT NOT NULL,
              brand TEXT NOT NULL,
              factory_year INTEGER NOT NULL,
              model_year INTEGER NOT NULL,
              plate TEXT NOT NULL UNIQUE,
              price REAL NOT NULL,
              photo TEXT)''')

conn.commit()
conn.close()

print("Banco de dados e tabela de carros criados com sucesso.")