import mysql.connector

try:
    # No XAMPP a senha é vazia, então deixamos ''
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='' 
    )

    cursor = conexao.cursor()

    # Criando o banco de dados (SQL puro via Python!)
    cursor.execute("CREATE DATABASE IF NOT EXISTS sistema_pedro;")
    cursor.execute("USE sistema_pedro;")

    # Criando uma tabela de usuários
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100),
            email VARCHAR(100)
        );
    """)

    print("✅ Banco 'sistema_pedro' e tabela 'usuarios' prontos!")

except Exception as erro:
    print(f"❌ Erro: {erro}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()