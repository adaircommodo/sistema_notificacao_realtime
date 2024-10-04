import psycopg2
from psycopg2 import OperationalError
from datetime import datetime

# Função para conectar ao banco de dados PostgreSQL
def conectar_postgres():
    try:
        connection = psycopg2.connect(
            host="localhost",  # Substitua pelo endpoint do RDS se estiver usando AWS
            user="seu_usuario",
            password="sua_senha",
            dbname="notificacoes_db"
        )
        print("Conectado ao PostgreSQL com sucesso!")
        return connection
    except OperationalError as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None

# Função para registrar notificações no PostgreSQL
def registrar_notificacao_postgres(descricao):
    try:
        conn = conectar_postgres()
        if conn is None:
            print("Conexão ao PostgreSQL falhou, abortando o registro.")
            return
        
        cursor = conn.cursor()
        sql_query = "INSERT INTO notificacoes (descricao, data_hora) VALUES (%s, %s)"
        valores = (descricao, datetime.now())

        cursor.execute(sql_query, valores)
        conn.commit()

        print(f"Notificação '{descricao}' registrada no PostgreSQL com sucesso.")
    except OperationalError as e:
        print(f"Erro ao registrar notificação no PostgreSQL: {e}")
    finally:
        if conn is not None and conn.closed == 0:
            cursor.close()
            conn.close()
            print("Conexão com PostgreSQL encerrada.")

# Exemplo de uso
if __name__ == "__main__":
    registrar_notificacao_postgres("Teste de notificação")
