import mysql.connector

# Dados que queremos salvar (Imagine que vieram de um formulário)
nome_usuario = str(input('Digite o seu nome: '))
email_usuario = str(input('Digite o seu email: '))

try:
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sistema_pedro'
    )
    cursor = conexao.cursor()

    # O comando SQL com 'placeholders' (%s) por segurança
    sql = "INSERT INTO usuarios (nome, email) VALUES (%s, %s)"
    valores = (nome_usuario, email_usuario)

    cursor.execute(sql, valores)
    
    # IMPORTANTE: No MySQL, para salvar alterações, precisa do commit!
    conexao.commit()

    print(f"✅ {cursor.rowcount} registro(s) inserido(s) com sucesso!")

except Exception as erro:
    print(f"❌ Erro ao inserir: {erro}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()