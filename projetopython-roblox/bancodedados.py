import sqlite3

# Conecta (e cria se não existir) ao banco de dados 'escola.db'
conexao = sqlite3.connect('escola.db')
cursor = conexao.cursor()

# Comando para criar a tabela de alunos
cursor.execute("""
CREATE TABLE IF NOT EXISTS alunos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    disciplina TEXT NOT NULL,
    nota REAL NOT NULL
);
""")

print("Banco de dados 'escola.db' e tabela 'alunos' criados com sucesso.")

# Fecha a conexão
conexao.close()