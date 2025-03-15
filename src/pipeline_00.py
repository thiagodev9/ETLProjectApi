import time
import requests
import os
import logging
import logfire
from dotenv import load_dotenv
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, BitcoinPreco
from logging import basicConfig, getLogger

# ------------------------------------------------------
# Configuração Logfire
logfire.configure()
basicConfig(handlers=[logfire.LogfireLoggingHandler()])
logger = getLogger(__name__)
logger.setLevel(logging.INFO)
logfire.instrument_requests()
logfire.instrument_sqlalchemy()

# ------------------------------------------------------

load_dotenv()

POSTGRES_USER = os.getenv('POSTGRES_USER') 
POSTGRES_HOST = os.getenv('POSTGRES_HOST') 
POSTGRES_PORT = os.getenv('POSTGRES_PORT') 
POSTGRES_DB = os.getenv('POSTGRES_DB') 
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD') 

DATABASE_URL = (
    f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}'
    f'@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'
)

# Cria o engine e a sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

"""Cria a tabela no banco d dados, se não existir."""
def criar_tabela():
    Base.metadata.create_all(engine)
    logger.info("Tabela criada/verificada com sucesso!")

def extract_dados_bitcoin():
    url = 'https://api.coinbase.com/v2/prices/spot'
    response = requests.get(url)
    if response.status_code==200:
        return response.json()
    else:
        logger.error(f"Erro na API: {response.status_code}")
        return None
    dados = response.json()
    return dados

def transform_dados_bitcoin(dados_json):
    valor = float(dados_json['data']['amount'])
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    timestamp = datetime.now()

    dados_transformados = {
        'valor': valor,
        'criptomoeda': criptomoeda,
        'moeda': moeda, 
        'timestamp': timestamp
    }
    
    return dados_transformados

def salvar_dados_postgres(dados):
    session = Session()
    novo_registro = BitcoinPreco(**dados)
    session.add(novo_registro)
    session.commit()
    session.close()
    logger.info(f"[{dados['timestamp']}] Dados salvos no PostgresSQL!")

if __name__=="__main__":
    criar_tabela()
    logger.info("Iniciando ETL com atualização a cada 15 segundos...(ctrl+c para interromper)")    
    #extração dos dados
    while True:
        try:
            dados_json = extract_dados_bitcoin()
            if dados_json:
                dados_tratados = transform_dados_bitcoin(dados_json)
                salvar_dados_postgres(dados_tratados)
            time.sleep(15)
        except KeyboardInterrupt:
            logger.info("\nProcesso interrompido pelo usuário")  
            break  
        except Exception as e:
            logger.error(f"Erro durante a execução: {e}")
            time.sleep(15)
 
#instalar tinydb

