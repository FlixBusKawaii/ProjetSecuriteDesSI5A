from ..extensions import db_auth

class Auth(db_auth.Model):
    __tablename__ = 'auth'
    id = db_auth.Column(db_auth.Integer, primary_key=True)
    last_name = db_auth.Column(db_auth.String(100), nullable=False)
    adresse = db_auth.Column(db_auth.String(100))
    num_phone = db_auth.Column(db_auth.String(10))
    hashed_password = db_auth.Column(db_auth.String(255), nullable=False)
    salt = db_auth.Column(db_auth.String(255), nullable=False)