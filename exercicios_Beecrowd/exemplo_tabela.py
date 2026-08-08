import sqlite3
'''
# 1. Conectar ao banco de dados (ou criar se não existir)
conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

# 2. Criar a tabela Produto
cursor.execute("""
CREATE TABLE IF NOT EXISTS Produto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    NomeProduto TEXT NOT NULL,
    Preco REAL NOT NULL
)
""")

# 3. Inserir 10 produtos (se ainda não existirem)
produtos = [
    ("Notebook Lenovo", 3500.00),
    ("Smartphone Samsung", 2200.00),
    ("Headset Gamer", 350.00),
    ("Teclado Mecânico", 420.00),
    ("Mouse Gamer", 250.00),
    ("Monitor LG 24\"", 899.90),
    ("Impressora HP", 780.50),
    ("Cadeira Gamer", 1200.00),
    ("HD Externo 1TB", 420.00),
    ("Pendrive 64GB", 60.00),
]

cursor.executemany("INSERT INTO Produto (NomeProduto, Preco) VALUES (?, ?)", produtos)

# 4. Salvar as alterações
conexao.commit()

# 5. Consultar e exibir os produtos
cursor.execute("SELECT * FROM Produto")
for linha in cursor.fetchall():
    print(linha)

# 6. Fechar conexão
conexao.close()
'''
<Produtos>
    <Produto id="1">
        <NomeProduto>Notebook Lenovo</NomeProduto>
        <Preco>3500.00</Preco>
    </Produto>
    <Produto id="2">
        <NomeProduto>Smartphone Samsung</NomeProduto>
        <Preco>2200.00</Preco>
    </Produto>
    <Produto id="3">
        <NomeProduto>Headset Gamer</NomeProduto>
        <Preco>350.00</Preco>
    </Produto>
    <Produto id="4">
        <NomeProduto>Teclado Mecânico</NomeProduto>
        <Preco>420.00</Preco>
    </Produto>
    <Produto id="5">
        <NomeProduto>Mouse Gamer</NomeProduto>
        <Preco>250.00</Preco>
    </Produto>
    <Produto id="6">
        <NomeProduto>Monitor LG 24"</NomeProduto>
        <Preco>899.90</Preco>
    </Produto>
    <Produto id="7">
        <NomeProduto>Impressora HP</NomeProduto>
        <Preco>780.50</Preco>
    </Produto>
    <Produto id="8">
        <NomeProduto>Cadeira Gamer</NomeProduto>
        <Preco>1200.00</Preco>
    </Produto>
    <Produto id="9">
        <NomeProduto>HD Externo 1TB</NomeProduto>
        <Preco>420.00</Preco>
    </Produto>
    <Produto id="10">
        <NomeProduto>Pendrive 64GB</NomeProduto>
        <Preco>60.00</Preco>
    </Produto>
</Produtos>

