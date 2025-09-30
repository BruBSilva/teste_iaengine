import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    # DB
    PORT = int(os.getenv("PORT", 5050))
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"
    APP_NAME = os.getenv("APP_NAME", "IA-ENGINE")
    INSTANCE_ID = os.getenv("INSTANCE_ID", "iaengine-1")
    HOST = os.getenv("HOST", "localhost")

    # Banco de dados
    DATABASE_URL = os.getenv("DATABASE_URL")
    if not DATABASE_URL:
        DB_USER = os.getenv("DB_USER", "postgres")
        DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
        DB_HOST = os.getenv("DB_HOST", "localhost")
        DB_PORT = os.getenv("DB_PORT", "5432")
        DB_NAME = os.getenv("DB_NAME", "iaengine")
        DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
