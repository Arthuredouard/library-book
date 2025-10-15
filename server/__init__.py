# server/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from .config import Config

# ------------------- EXTENSIONS -------------------
db = SQLAlchemy()
migrate = Migrate()
cors = CORS()

# ------------------- APPLICATION FACTORY -------------------
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialiser les extensions
    db.init_app(app)
    migrate.init_app(app, db)
    cors.init_app(app)

    # Importer les modèles et routes après l'init pour éviter les imports circulaires
    from . import models
    from . import routes

    return app


