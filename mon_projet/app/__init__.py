from flask import Flask
from .extensions import init_dbs
from .routes import Auth, Users
from config.database import DevelopmentConfig
from .routes.api import api_bp

def create_app(config_class=DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    app.register_blueprint(api_bp)  # Enregistre toutes les routes sous /api
    
    # Initialiser les bases de données
    init_dbs(app)
    
    # Enregistrer les blueprints
    app.register_blueprint(Auth, url_prefix='/auth')
    app.register_blueprint(Users, url_prefix='/users')
    
    # Créer les tables dans chaque base
    with app.app_context():
        Auth.create_all()
        Users.create_all()
    
    return app