from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .users import Users
from .auth import Auth

def init_app(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
