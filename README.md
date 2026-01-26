# NutriFood
NutriFood est une application web Django qui permet de rechercher des produits alimentaires et de proposer une alternative plus saine basée sur le Nutri-Score et la catégorie du produit.

Le projet s’appuie sur des données issues de l’API OpenFoodFacts.

## Fonctionnalités
- Recherche de produits par nom ou catégorie
- Page de détail d’un produit
- Proposition automatique d’un substitut plus sain
- Algorithme simple basé sur le Nutri-Score
- Interface moderne en HTML/CSS
- Commande de gestion pour importer les produits
- Tests Django (modèles, vues, logique métier)

## Stack technique
- Backend : Django 5.2
- Base de données : PostgreSQL
- Frontend : HTML5, CSS3
- Données : OpenFoodFacts API
- Tests : Django TestCase
- Versioning : Git / GitHub

## Installation
> Cloner le projet
git clone https://github.com/TomLEPERT/NutriFood.git
cd NutriFood/backend

> Créer et activer un environnement virtuel
python -m venv venv
source venv/Scripts/activate
# ou
source venv/bin/activate

> Installer les dépendances
pip install -r requirements.txt

> Configurer la base de données

Dans config/settings.py :

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nutrifood',
        'USER': 'app_user',
        'PASSWORD': 'your_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

Puis :

python manage.py migrate

> Importer les produits depuis OpenFoodFacts
python manage.py maj_bdd_opfofa

> Lancer le serveur
python manage.py runserver

Accès :

http://127.0.0.1:8000/

## Utilisation

Aller sur la page d’accueil
- Rechercher un produit
- Visualiser la liste des produits
- Voir le produit de référence
- Découvrir une alternative plus saine proposée par NutriFood

## Algorithme de substitution
L’algorithme :
- Prend le premier produit trouvé comme référence

Recherche des produits :
- de catégorie proche
- avec un meilleur Nutri-Score

Classe les candidats par :
- Nutri-Score
- Nom
- Propose le meilleur résultat

## Lancer les tests
python manage.py test

## Interface
- Layout responsive
- Badges Nutri-Score colorés
- Cartes produit
- Suggestion visuelle de substitut

## Améliorations possibles
- Pagination des résultats
- Authentification utilisateur
- Sauvegarde de favoris
- Historique de recherches
- Filtrage par catégorie
- Score nutritionnel plus précis
- API REST (Django Rest Framework)

## Auteur
Tom Lepert
Projet réalisé dans le cadre de la formation Data Analyst – Simplon

## Licence
Projet éducatif – libre d’utilisation et de modification.