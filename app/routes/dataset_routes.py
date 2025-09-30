from flask import Blueprint, request, jsonify
from ..services import dataset_service
from ..schemas.dataset_schema import dataset_schema, datasets_schema

dataset_bp = Blueprint("dataset", __name__, url_prefix="/datasets")

@dataset_bp.route("/", methods=["GET"])
def listar():
    datasets = dataset_service.listar_datasets()
    return jsonify(datasets_schema.dump(datasets))

@dataset_bp.route("/<int:dataset_id>", methods=["GET"])
def obter(dataset_id):
    dataset = dataset_service.obter_dataset(dataset_id)
    if not dataset:
        return jsonify({"erro": "Dataset não encontrado"}), 404
    return dataset_schema.jsonify(dataset)

@dataset_bp.route("/", methods=["POST"])
def criar():
    data = request.get_json()
    dataset = dataset_service.criar_dataset(data)
    return jsonify(dataset_schema.dump(dataset)), 201

@dataset_bp.route("/<int:dataset_id>", methods=["PUT"])
def atualizar(dataset_id):
    data = request.get_json()
    dataset = dataset_service.atualizar_dataset(dataset_id, data)
    if not dataset:
        return jsonify({"erro": "Dataset não encontrado"}), 404
    return jsonify(dataset_schema.dump(dataset))

@dataset_bp.route("/<int:dataset_id>", methods=["DELETE"])
def deletar(dataset_id):
    dataset = dataset_service.deletar_dataset(dataset_id)
    if not dataset:
        return jsonify({"erro": "Dataset não encontrado"}), 404
    return jsonify({"mensagem": "Dataset deletado com sucesso"})
