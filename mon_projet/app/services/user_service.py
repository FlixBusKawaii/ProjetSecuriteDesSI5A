from ..models.users import Users  # Import du modèle User
from ..extensions import db_users  # Connexion à la base de données 'users'

class UserService:
    @staticmethod
    def get_user_by_id(user_id):
        """ Récupère un utilisateur par son ID """
        return Users.query.get(user_id)

    @staticmethod
    def create_user(username):
        """ Crée un nouvel utilisateur """
        new_user = Users(username=username)
        db_users.session.add(new_user)
        db_users.session.commit()
        return new_user

    @staticmethod
    def update_username(user_id, new_username):
        """ Met à jour le nom d'utilisateur """
        user = Users.query.get(user_id)
        if user:
            user.username = new_username
            db_users.session.commit()
            return user
        return None

    @staticmethod
    def delete_user(user_id):
        """ Supprime un utilisateur """
        user = Users.query.get(user_id)
        if user:
            db_users.session.delete(user)
            db_users.session.commit()
            return True
        return False
