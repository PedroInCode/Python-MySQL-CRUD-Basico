import mysql.connector

try:
    conexao = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='sistema_pedro'
    )
    cursor = conexao.cursor()

    # Comando para selecionar tudo
    cursor.execute("SELECT * FROM usuarios")

    # O fetchall() "pega" todos os resultados que o cursor encontrou
    resultados = cursor.fetchall()

    print("\n--- LISTA DE USUÁRIOS CADASTRADOS ---")
    for linha in resultados:
        print(f"ID: {linha[0]} | Nome: {linha[1]} | Email: {linha[2]}")

except Exception as erro:
    print(f"❌ Erro ao listar: {erro}")

finally:
    if 'conexao' in locals() and conexao.is_connected():
        cursor.close()
        conexao.close()