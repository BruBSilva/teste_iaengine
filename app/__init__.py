from flask import Flask
from .config import Config
from .routes.dataset_routes import dataset_bp
from .routes.dados_routes import dados_bp
from .extensions import db

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = Config.DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    #migrate.init_app(app, db)

    app.register_blueprint(dataset_bp)
    app.register_blueprint(dados_bp)

    return app