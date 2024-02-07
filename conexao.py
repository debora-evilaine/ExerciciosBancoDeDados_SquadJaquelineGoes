import sqlite3


mercado = sqlite3.connect('mercados')
cursor = mercado.cursor()

# CRIAÇÃO DE TABELAS:
cursor.execute('DROP TABLE  IF EXISTS Produtos')
cursor.execute('DROP TABLE IF EXISTS Clientes')
cursor.execute('DROP TABLE IF EXISTS Vendas')


cursor.execute(
    'CREATE TABLE Clientes(clienteID INT PRIMARY KEY , nome VARCHAR(50),telefone varchar(11), endereco VARCHAR(80));')
cursor.execute(
    'CREATE TABLE Produtos(produtoID INT PRIMARY KEY, nome VARCHAR(50), categoria VARCHAR(50), estoque INT);')
cursor.execute('CREATE TABLE Vendas(vendasID PRIMARY KEY, cliente_id INT, produto_id INT, quantidade INT, FOREIGN KEY (cliente_id) REFERENCES Clientes(clienteID), FOREIGN KEY (produto_id) REFERENCES Produtos(produtoID))')


# INSERÇÃO DE DADOS:
cursor.execute(
    'INSERT INTO Clientes(clienteID,nome,telefone,endereco) VALUES (1,"Ana" , 1111111, "Rua 123")')
cursor.execute(
    'INSERT INTO Clientes(clienteID,nome, telefone, endereco) VALUES (2,"Ano" , 222222, "Rua 321")')
cursor.execute(
    'INSERT INTO Clientes(clienteID,nome,telefone,endereco) VALUES (3, "João", 33333333, "Rua abc")')
cursor.execute(
    'INSERT INTO Clientes(clienteID,nome,telefone,endereco) VALUES (4, "Maria", 34857832, "Rua cba")')


cursor.execute(
    'INSERT INTO Produtos(produtoID,nome,categoria,estoque) VALUES (1, "Fone de ouvido", "Eletrônicos", 50)')
cursor.execute(
    'INSERT INTO Produtos(produtoID,nome,categoria,estoque) VALUES (2, "Miojo", "Comida", 500)')
cursor.execute(
    'INSERT INTO Produtos(produtoID,nome,categoria,estoque) VALUES (3, "Arroz", "Comida", 100)')
cursor.execute(
    'INSERT INTO Produtos(produtoID,nome,categoria,estoque) VALUES (4, "Feijão", "Comida", 390)')
cursor.execute(
    'INSERT INTO Produtos(produtoID,nome,categoria,estoque) VALUES(5, "Prato", "Cozinha", 0)')

cursor.execute(
    'INSERT INTO Vendas(vendasID, cliente_id, produto_id, quantidade) VALUES (1, 3, 2, 3)')

# CONSULTAS:

produtosEmEstoque = cursor.execute('SELECT * FROM Produtos WHERE estoque > 0')
for produto in produtosEmEstoque:
    print(produto)

vendasPorCliente = cursor.execute(
    'SELECT Clientes.nome AS nome_cliente, Produtos.nome AS nome_produto, Vendas.quantidade FROM Vendas JOIN Clientes ON Vendas.cliente_id = Clientes.clienteID JOIN Produtos ON Vendas.produto_id = Produtos.produtoID WHERE Vendas.cliente_id = 3')
for venda in vendasPorCliente:
    print(venda)


totalVendasPorCategoria = cursor.execute(
    'SELECT Produtos.categoria, SUM(Vendas.quantidade) AS total_vendas FROM Vendas JOIN Produtos ON Vendas.produto_id = Produtos.produtoID GROUP BY Produtos.categoria')
for total_vendas_categoria in totalVendasPorCategoria:
    print(total_vendas_categoria)


produtosMaisVendidos = cursor.execute(
    'SELECT Produtos.nome, SUM(Vendas.quantidade) AS total_vendas FROM Vendas JOIN Produtos ON Vendas.produto_id = Produtos.produtoID GROUP BY Produtos.nome ORDER BY total_vendas DESC')
for produto_mais_vendido in produtosMaisVendidos:
    print(produto_mais_vendido)


# ATUALIZAÇÃO:
# diminui a quantidade em estoque do produto com produtoID 2 em 3
atualizarQuantidade = cursor.execute(
    'UPDATE Produtos SET estoque = estoque - 3 WHERE produtoID = 2')
mercado.commit()
print("Quantidade em estoque atualizada com sucesso.")

# remove um cliente com clienteID 4 do banco de dados
removerCliente = cursor.execute('DELETE FROM Clientes WHERE clienteID = 4')
mercado.commit()
print("Cliente removido com sucesso.")


mercado.commit()
mercado.close
