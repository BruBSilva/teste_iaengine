from ..models.dataset_dados import Dataset
from ..extensions import db

def listar_datasets():
    return Dataset.query.order_by(Dataset.id.asc()).all()

def obter_dataset(dataset_id):
    return Dataset.query.get(dataset_id)

def criar_dataset(data):
    dataset = Dataset(**data)
    db.session.add(dataset)
    db.session.commit()
    return dataset

def atualizar_dataset(dataset_id, data):
    dataset = Dataset.query.get(dataset_id)
    if not dataset:
        return None
    for key, value in data.items():
        setattr(dataset, key, value)
    db.session.commit()
    return dataset

def deletar_dataset(dataset_id):
    dataset = Dataset.query.get(dataset_id)
    if not dataset:
        return None
    db.session.delete(dataset)
    db.session.commit()
    return dataset
