from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    # 🔥 IMPORTANT — importer les modèles ici
    from app.models.user import User

    from app.auth.routes import auth
    app.register_blueprint(auth)

    return app
