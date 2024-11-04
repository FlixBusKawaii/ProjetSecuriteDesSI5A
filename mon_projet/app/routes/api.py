from flask import Blueprint
from .user_routes import user_bp
from .auth_routes import auth_bp

# Création d'un blueprint principal pour l'API
api_bp = Blueprint('api', __name__, url_prefix='/api')

# Enregistrement des sous-blueprints
api_bp.register_blueprint(user_bp, url_prefix='/users')
api_bp.register_blueprint(auth_bp, url_prefix='/auth')
