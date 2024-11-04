from ..extensions import db_users

class Users(db_users.Model):
    __bind_key__ = 'users'  # Spécifie le lien avec la base `users`
    __tablename__ = 'users'
    id = db_users.Column(db_users.Integer, primary_key=True)
    username = db_users.Column(db_users.String(100), nullable=False)