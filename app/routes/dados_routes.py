import base64

from flask import Blueprint, request, jsonify
from ..services import dados_service
from ..schemas.dados_schema import dados_schema, multi_dados_schemas

dados_bp = Blueprint("dados", __name__, url_prefix="/dados")

@dados_bp.route("/", methods=["GET"])
def listar():
    multi_dados = dados_service.listar_dados()
    return jsonify(multi_dados_schemas.dump(multi_dados))

@dados_bp.route("/<int:dados_id>", methods=["GET"])
def obter(dados_id):
    dados = dados_service.obter_dados(dados_id)
    if not dados:
        return jsonify({"erro": "Dados não encontrados"}), 404
    return dados_schema.jsonify(dados)

@dados_bp.route("/", methods=["POST"])
def criar():
    data = request.get_json()
    data["arquivo_csv"] = base64.b64decode(data["arquivo_csv"])
    dados = dados_service.criar_dados(data)
    return jsonify(dados_schema.dump(dados)), 201

@dados_bp.route("/<int:dados_id>", methods=["PUT"])
def ampliar_dados(dados_id):
    data = request.get_json()
    dados = dados_service.ampliar_dados(dados_id, data)
    if not dados:
        return jsonify({"erro": "Dataset não encontrado"}), 404
    return jsonify(dados_schema.dump(dados))

@dados_bp.route("/<int:dados_id>", methods=["DELETE"])
def deletar(dados_id):
    dados = dados_service.deletar_dados(dados_id)
    if not dados:
        return jsonify({"erro": "Dados não encontrados"}), 404
    return jsonify({"mensagem": "Dados deletados com sucesso"})