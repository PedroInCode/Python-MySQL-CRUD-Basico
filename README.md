# Integração Python + MySQL (CRUD Básico) 🐍🗄️

Este projeto faz parte dos meus estudos práticos de Back-end. Aqui, aprendi a conectar o Python ao banco de dados MySQL utilizando o ambiente XAMPP.

## 🧠 O que eu aprendi (Guia de Comandos)

Para não esquecer a lógica da integração, organizei os principais comandos que utilizei:

| Comando | Para que serve? |
| :--- | :--- |
| `mysql.connector.connect()` | Estabelece a ponte entre o script Python e o servidor MySQL. |
| `cursor()` | É o "agente" que executa as instruções SQL dentro do banco. |
| `execute()` | Onde passamos o comando SQL puro (Ex: INSERT, SELECT). |
| `commit()` | **Essencial:** Confirma e salva permanentemente as alterações no banco. |
| `fetchall()` | Captura todos os registros retornados por uma consulta (SELECT). |

## 🚀 Como testar os scripts
1. Inicie o **MySQL** através do painel do XAMPP.
2. Certifique-se de ter o driver instalado: `pip install mysql-connector-python`.
3. Rode o script `01_criar_banco.py` primeiro para configurar o ambiente.
4. Use o `02_inserir_usuario.py` para cadastrar dados via terminal (`input`).
5. Visualize os resultados com o `03_listar_usuarios.py`.
