
# 📢 Sistema de Notificações em Tempo Real

## Descrição

Este projeto foi criado para demonstrar o poder do **Python** com **programação reativa**, utilizando a biblioteca **RxPY** para criar um **sistema de notificações em tempo real**. As notificações são geradas aleatoriamente e registradas em **bancos de dados MySQL e PostgreSQL**. Além disso, o projeto pode ser configurado para armazenar os dados no **AWS RDS**, permitindo maior escalabilidade e uso em ambientes de produção.

## 🚀 Funcionalidades

- Geração de notificações em tempo real. (que pode ser qualquer diretório, repositório, etc)
- Integração com bancos de dados MySQL e PostgreSQL (local e AWS RDS).
- Registro de notificações em tabelas de banco de dados com timestamps.
- Fácil configuração e execução.

## 🛠 Tecnologias Utilizadas

- **Python 3.8+**
- **RxPY** (Reactive Extensions for Python)
- **MySQL** (Local e AWS RDS)
- **PostgreSQL** (Local e AWS RDS)
- **mysql-connector-python** (Conector Python para MySQL)
- **psycopg2-binary** (Conector Python para PostgreSQL)

## 🎯 Objetivos do Projeto

- Demonstrar como implementar **programação reativa** em Python usando **RxPY**.
- Ensinar a integrar sistemas em tempo real com bancos de dados relacionais (MySQL e PostgreSQL).
- Fornecer uma solução flexível que funcione em ambientes locais e na nuvem (AWS RDS).

## 📂 Estrutura do Projeto

```bash
.
├── README.md
├── requirements.txt
└── src
    ├── notificacoes.py        # Código principal do sistema de notificações
    ├── db_mysql.py            # Funções de conexão e registro no MySQL
    └── db_postgres.py         # Funções de conexão e registro no PostgreSQL
```

## 🔧 Configuração e Instalação

### Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.8+
- Um servidor MySQL (local ou AWS RDS)
- Um servidor PostgreSQL (local ou AWS RDS)

### Instalar Dependências

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/adaircommodo/python_reativo_sistema_notificacao_realtime.git
cd python_reativo_sistema_notificacao_realtime
pip install -r requirements.txt
```

### Configurar MySQL e PostgreSQL

1. Crie as tabelas no MySQL e PostgreSQL:

**MySQL:**
```sql
CREATE DATABASE notificacoes_db;
USE notificacoes_db;
CREATE TABLE notificacoes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255),
    data_hora TIMESTAMP
);
```

**PostgreSQL:**
```sql
CREATE DATABASE notificacoes_db;
\c notificacoes_db
CREATE TABLE notificacoes (
    id SERIAL PRIMARY KEY,
    descricao VARCHAR(255),
    data_hora TIMESTAMP
);
```

2. Atualize os detalhes de conexão no arquivo `db_mysql.py` e `db_postgres.py` com as credenciais corretas para o seu banco de dados local ou AWS RDS.

```python
# Exemplo de db_mysql.py
def conectar_mysql():
    return mysql.connector.connect(
        host="localhost",  # ou endpoint do RDS
        user="seu_usuario",
        password="sua_senha",
        database="notificacoes_db"
    )

# Exemplo de db_postgres.py
def conectar_postgres():
    return psycopg2.connect(
        host="localhost",  # ou endpoint do RDS
        user="seu_usuario",
        password="sua_senha",
        dbname="notificacoes_db"
    )
```

## 🏃‍♂️ Executar o Projeto

Para executar o sistema de notificações em tempo real:

```bash
python src/notificacoes.py
```

Você verá as notificações sendo geradas e registradas no console e no banco de dados configurado. O sistema emitirá notificações a cada 2 segundos.

Exemplo de saída:

```bash
Recebida: Notificação: Sucesso em 2024-10-04 12:34:56
Registrando no MySQL...
Registrando no PostgreSQL...
```

## 🌐 Configuração para AWS RDS

Se estiver utilizando o **AWS RDS**:

1. Crie uma instância de banco de dados MySQL/PostgreSQL no RDS.
2. Obtenha o **endpoint** da instância e substitua no código de conexão.
3. Certifique-se de que as regras de segurança permitem a conexão de sua máquina local ao RDS.
4. Execute o projeto normalmente.

## 📊 Testando a Integração com Banco de Dados

Após a execução do sistema, verifique as notificações registradas no banco de dados:

**MySQL:**
```sql
SELECT * FROM notificacoes;
```

**PostgreSQL:**
```sql
SELECT * FROM notificacoes;
```

## 📖 Próximos Passos

- Adicionar mais funcionalidades de notificação.
- Implementar diferentes tipos de Observers e filtros para processar dados de diferentes fontes.
- Escalar o sistema para integrar com serviços de mensageria como **Kafka** ou **RabbitMQ**.

## 📝 Licença

Este projeto é licenciado sob a [MIT License](LICENSE).

---

_Feito com ❤️ por [Adair J. Rossatto Commodo](https://github.com/adaircommodo)_
