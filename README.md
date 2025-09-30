# teste_iaengine-python

## ****Esta é uma API em Python Flask****

## Configuração e Execução

Siga os passos abaixo para ter a aplicação funcionando em seu ambiente local.

### 1. (Opcional) Crie um Ambiente Virtual

O uso de um ambiente virtual é fortemente recomendado para isolar as dependências do projeto, mas não é estritamente obrigatório. Se optar por não usar, as dependências serão instaladas globalmente.

```bash
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente (Windows)
.\venv\Scripts\activate

# Ative o ambiente (Linux/macOS)
# source venv/bin/activate
```

### 2. Instale as Dependências

Instale todas as bibliotecas Python necessárias.

```bash
pip install -r requirements.txt
```

### 3. Configure as Variáveis de Ambiente

A aplicação precisa das credenciais para se conectar aos outros serviços e criar o banco de dados automaticamente.

**a. Crie o arquivo `.env`:**
Crie o arquivo `.env` a partir do `.env_exemplo`

### 4. Criação do Banco de Dados

Antes de executar a aplicação pela primeira vez, é necessário criar o banco de dados, os scripts estão no arquivo `anotacoes.txt`

### 6. Execute a Aplicação

Com o banco de dados criado, inicie a API:

```bash
python app.py
```

### 7. Teste a API

O arquivo `exemplos_json.txt` possui exemplos de body para as requisições de criação de datasets e dados