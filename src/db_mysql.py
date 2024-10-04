import mysql.connector
from mysql.connector import Error
from datetime import datetime

# Função para conectar ao banco de dados MySQL
def conectar_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Substitua pelo endpoint do RDS se usar AWS
            user="seu_usuario",
            password="sua_senha",
            database="notificacoes_db"
        )
        if connection.is_connected():
            print("Conectado ao MySQL com sucesso!")
        return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None

# Função para registrar notificações no MySQL
def registrar_notificacao_mysql(descricao):
    try:
        conn = conectar_mysql()
        if conn is None:
            print("Conexão ao MySQL falhou, abortando o registro.")
            return
        
        cursor = conn.cursor()
        sql_query = "INSERT INTO notificacoes (descricao, data_hora) VALUES (%s, %s)"
        valores = (descricao, datetime.now())

        cursor.execute(sql_query, valores)
        conn.commit()

        print(f"Notificação '{descricao}' registrada no MySQL com sucesso.")
    except Error as e:
        print(f"Erro ao registrar notificação no MySQL: {e}")
    finally:
        if conn is not None and conn.is_connected():
            cursor.close()
            conn.close()
            print("Conexão com MySQL encerrada.")

# Exemplo de uso
if __name__ == "__main__":
    registrar_notificacao_mysql("Teste de notificação")
