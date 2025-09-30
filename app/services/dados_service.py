from ..models.dataset_dados import Dados
from ..extensions import db
from io import BytesIO, StringIO
import pandas as pd

def listar_dados():
    return Dados.query.order_by(Dados.id.asc()).all()

def obter_dados(dados_id):
    return Dados.query.get(dados_id)

def criar_dados(data):
    dados = Dados(**data)
    db.session.add(dados)
    db.session.commit()
    return dados

def ampliar_dados(dados_id, dados_novos):
    dados = Dados.query.get(dados_id)

    # Converte DTO em DataFrame
    df_novos = pd.DataFrame([d.dict() for d in dados_novos.arquivo_csv])
    df_novos = aplicar_tipos(df_novos, dados.metadados)

    # Lê CSV existente
    csv_bytes = BytesIO(dados.arquivo_csv)
    df_existente = pd.read_csv(csv_bytes)

    # Concatena os novos dados
    df_atualizado = pd.concat([df_existente, df_novos], ignore_index=True)
    df_atualizado = aplicar_tipos(df_atualizado, dados.metadados)

    # Salva de volta em bytes
    buffer = StringIO()
    df_atualizado.to_csv(buffer, index=False)
    dados.arquivo_csv = buffer.getvalue().encode("utf-8")

    db.session.commit()
    return dados

def deletar_dados(dados_id):
    dados = Dados.query.get(dados_id)
    if not dados:
        return None
    db.session.delete(dados)
    db.session.commit()
    return dados

def aplicar_tipos(df, metadados):
    tipo_map = {
        "int": "Int64",   # int nativo com suporte a NaN
        "float": "float",
        "str": "string"
    }
    for coluna, info in metadados.items():
        if coluna in df.columns:
            df[coluna] = df[coluna].astype(tipo_map[info["tipo"]])
    return df