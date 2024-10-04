import rx
from rx import operators as ops
from datetime import datetime
import random
import time

# Importando as funções de registro do MySQL e PostgreSQL
from db_mysql import registrar_notificacao_mysql
from db_postgres import registrar_notificacao_postgres

# Simulando um gerador de notificações
def gerar_notificacao():
    status = random.choice(["Sucesso", "Falha", "Processando"])
    return f"Notificação: {status} em {datetime.now()}"

# Criando um Observable que emite notificações a cada 2 segundos
observable = rx.interval(2).pipe(
    ops.map(lambda i: gerar_notificacao())
)

# Função para lidar com as notificações recebidas e registrar no banco de dados
def notificar(notificacao):
    print(f"Recebida: {notificacao}")
    
    # Registrando a notificação no MySQL
    registrar_notificacao_mysql(notificacao)

    # Registrando a notificação no PostgreSQL
    registrar_notificacao_postgres(notificacao)

# Subscrição ao Observable para receber notificações
observable.subscribe(on_next=notificar)

# Manter o script em execução por 10 segundos para ver as notificações
time.sleep(10)
