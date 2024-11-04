class DatabaseConfig:
    # Configuration commune
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Base de données d'authentification
    SQLALCHEMY_DATABASE_URI_AUTH = 'mysql://username:password@localhost/authentification'
    
    # Base de données utilisateurs
    SQLALCHEMY_DATABASE_URI_USERS = 'mysql://username:password@localhost/users'

# Configuration pour le développement
class DevelopmentConfig(DatabaseConfig):
    DEBUG = True
    SECRET_KEY = 'dev-secret-key'

# Configuration pour la production
class ProductionConfig(DatabaseConfig):
    DEBUG = False
    SECRET_KEY = 'prod-secret-key'  # À changer en production !