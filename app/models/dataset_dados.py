from ..extensions import db
from datetime import datetime, timezone
from sqlalchemy.dialects.postgresql import JSONB

class Dataset(db.Model):
    __tablename__ = "dataset"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(255))
    datacriacao = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    # Relacionamento com os dados
    dados = db.relationship("Dados", back_populates="dataset", cascade="all, delete-orphan")

class Dados(db.Model):
    __tablename__ = "dados"

    id = db.Column(db.Integer, primary_key=True)
    dataset_id = db.Column(db.Integer, db.ForeignKey("dataset.id"), nullable=False)
    arquivo_csv = db.Column(db.LargeBinary, nullable=False)  # equivale ao BYTEA
    metadados_json = db.Column(JSONB, nullable=False) # usa JSONB no Postgres
    tratamentos_json = db.Column(JSONB, nullable=False)
    data_atualizacao = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    # Relacionamento inverso
    dataset = db.relationship("Dataset", back_populates="dados")
