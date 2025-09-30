from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.dataset_dados import Dados

class DatasetSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Dados
        load_instance = True
        include_fk = True

dados_schema = DatasetSchema()
multi_dados_schemas = DatasetSchema(many=True)