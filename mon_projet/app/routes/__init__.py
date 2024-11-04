import sys
import os

models_path = os.path.abspath(os.path.join(os.path.dirname(__file__),'..', 'models'))
if models_path not in sys.path:
    sys.path.append(models_path)

from models import Users, Auth

# Permet d'importer directement depuis app.routes
__all__ = ['Users', 'Auth']