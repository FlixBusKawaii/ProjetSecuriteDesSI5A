# ProjetSecuriteDesSI5A
Projet: Système d’annuaire sécurisé

# Chaque équipe projet devra rendre:

- Spécification logicielle
- Use cases
- Architecture
- Structure des données
- Spécification de l’architecture
- Configuration des serveurs
- Politique de sécurité
- Détails des flux entre les systèmes
- Gestion du code source et contrôle de version
  - Un dépôt git par système/sous système
  - branches master/develop
  - Pipeline CI/CD
    - Build
    - Test
    - Deploy
- Compte rendu de réalisation
- Document académique relatant vos choix et décrivant le déroulement de votre projet
- Inclure les livrables décrits en annexe

## L’annuaire sécurisé proposera ces fonctionnalités:

### Outils d'administration
- Ajouter manuellement un utilisateur
- Changer un mot de passe
- Promouvoir/Rétrograder un utilisateur
- Supprimer un utilisateur

### Service d’annuaire
- Lister les utilisateurs du système
- Seul un utilisateur connecté peut lister les autres utilisateurs
- Recherche basique

### Compte d’utilisateur
- Inscription
- Mise à jour du profil
- Connexion
- Déconnexion
- Clôture du compte

### Contraintes de sécurité:
- La base de données doit être sécurisée
- Les mots de passe doivent être protégés
- Le design doit respecter:
  - Les principes du moindre privilège
  - Les principes de défense en profondeur
  - Permettre la traçabilité des actions
  - Respecter les normes d’implémentation industrielles

Le projet contient peu de fonctionnalités mais elles doivent être rigoureusement développés et explicités.

### Contraintes technologiques:

#### Langages
- Python
- Java

#### Base de données
- Postgresql
- Mysql

#### Backend
- Django / Flask
- Apache Tomcat

#### Frontend
- Technologie libre de choix

#### Architecture réseau
- n-tiers

#### Hébergement
- Machines virtuelles VMware
- Containers



# Installation

1. Cloner le repository
```bash
git clone https://github.com/votre-username/votre-projet.git
cd votre-projet
```

2. Créer un environnement virtuel
```bash
python -m venv venv
```

3. Activer l'environnement virtuel
```bash
# Sur Windows
.\venv\Scripts\activate

# Sur Unix ou MacOS
source venv/bin/activate
```

4. Installer les dépendances
```bash
pip install -r requirements.txt
```

5. Configurer les variables d'environnement
```bash
cp .env.example .env
# Éditer le fichier .env avec vos propres valeurs
```

6. Initialiser la base de données
```bash
flask db upgrade
```

7. Lancer l'application
```bash
flask run
```