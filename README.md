# ETL com Python e Requests

Este projeto implementa um processo ETL (Extract, Transform, Load) utilizando Python e a biblioteca `requests` para extrair dados de uma API, transformá-los conforme necessário e carregá-los em um banco de dados.

## 🛠 Tecnologias Utilizadas
- Python 3.x
- Requests
- Pandas
- SQLAlchemy
- Banco de Dados (MySQL/PostgreSQL)

## 📌 Funcionalidades
- Extração de dados via API usando `requests`
- Transformação dos dados com `pandas`
- Carga dos dados em um banco de dados SQL
- Agendamento da execução do ETL

## 📂 Estrutura do Projeto
```
/etl_project
│── etl.py         # Script principal do ETL
│── config.py      # Configurações do projeto
│── requirements.txt  # Dependências do projeto
│── README.md      # Documentação do projeto
```

## 🚀 Como Executar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/etl-python.git
   cd etl-python
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure as credenciais da API e banco de dados no `config.py`.
4. Execute o script ETL:
   ```bash
   python etl.py
   ```

## ⚙ Configuração
Crie um arquivo `config.py` e adicione as seguintes configurações:
```python
API_URL = "https://api.exemplo.com/dados"
API_KEY = "sua-chave-aqui"

DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "user": "usuario",
    "password": "senha",
    "database": "meu_banco"
}
```

## 📌 Próximos Passos
- Implementar logging para monitoramento
- Criar testes automatizados
- Melhorar a eficiência do processamento

## 📄 Licença
Este projeto está sob a licença MIT.

