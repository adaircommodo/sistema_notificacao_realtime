import rx
from rx import operators as ops
import requests
from datetime import datetime
import time

# Importando as funções de registro do MySQL e PostgreSQL
from db_mysql import registrar_notificacao_mysql
from db_postgres import registrar_notificacao_postgres


#Welcome to Alpha Vantage! Your dedicated access key is: N5MR2VH9O6E5IBVE. Please record this API key at a safe place for future data access.

# Função para obter o preço atual da ação OIBR3 no mercado brasileiro
def obter_preco_acao(symbol):
    try:
        url = f"https://query1.finance.yahoo.com/v8/finance/chart/{symbol}?region=BR&lang=pt-BR"
        response = requests.get(url)
        
        # Verificando se a requisição foi bem-sucedida
        if response.status_code != 200:
            print(f"Erro ao buscar o preço da ação {symbol}. Código HTTP: {response.status_code}")
            print(f"Conteúdo retornado: {response.text}")
            return None

        # Convertendo a resposta em JSON
        data = response.json()

        # Verificando se a resposta contém os dados esperados
        if "chart" in data and "result" in data["chart"]:
            preco_atual = data["chart"]["result"][0]["meta"]["regularMarketPrice"]
            return preco_atual
        else:
            print(f"Formato inesperado de resposta: {data}")
            return None
    except requests.exceptions.JSONDecodeError as e:
        print(f"Erro ao decodificar JSON: {e}")
        print(f"Conteúdo retornado: {response.text}")
        return None
    except Exception as e:
        print(f"Erro ao buscar o preço da ação {symbol}: {e}")
        return None

# Função que gera a notificação com o preço da ação
def gerar_notificacao_preco(symbol):
    preco = obter_preco_acao(symbol)
    if preco is not None:
        return f"Ação {symbol}: preço atualizado em {datetime.now()}: R${preco:.2f}"
    else:
        return f"Falha ao obter o preço da ação {symbol} em {datetime.now()}"

# Criando um Observable que verifica o preço a cada 30 segundos
tempo_em_segundos = 30
symbol = "OIBR3.SA"  # Código da ação OIBR3 na B3 (mercado brasileiro)
observable = rx.interval(tempo_em_segundos).pipe(
    ops.map(lambda i: gerar_notificacao_preco(symbol))
)

# Função para lidar com as notificações e registrar no banco de dados
def notificar(notificacao):
    print(f"Recebida: {notificacao}")
    
    # Registrando a notificação no MySQL
    #registrar_notificacao_mysql(notificacao)

    # Registrando a notificação no PostgreSQL
    #registrar_notificacao_postgres(notificacao)

# Subscrição ao Observable para monitorar a ação e registrar notificações
observable.subscribe(on_next=notificar)

# Manter o script em execução por 1 minuto para ver as notificações
time.sleep(60)
