from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from app.models.dataset_dados import Dataset

class DatasetSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Dataset
        load_instance = True
        include_fk = True

dataset_schema = DatasetSchema()
datasets_schema = DatasetSchema(many=True)
