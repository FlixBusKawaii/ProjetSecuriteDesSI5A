from flask_sqlalchemy import SQLAlchemy

# Création des instances de base de données
db_auth = SQLAlchemy()
db_users = SQLAlchemy()

def init_dbs(app):
    # Configuration de la base auth
    app.config['SQLALCHEMY_DATABASE_URI'] = app.config['SQLALCHEMY_DATABASE_URI_AUTH']
    db_auth.init_app(app)
    
    # Configuration de la base users
    app.config['SQLALCHEMY_BINDS'] = {
        'users': app.config['SQLALCHEMY_DATABASE_URI_USERS']
    }
    db_users.init_app(app)