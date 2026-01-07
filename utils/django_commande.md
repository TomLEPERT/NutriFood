# Mémo des commandes Django

## Gestion du projet et des apps

### Créer un projet Django

- django-admin startproject nom_du_projet

### Créer une app dans le projet

- python manage.py startapp nom_de_lapp

### Lister toutes les apps installées

- python manage.py showmigrations

## Lancer le serveur de développement

### Serveur par défaut (localhost:8000)

- python manage.py runserver

### Serveur sur un port spécifique

- python manage.py runserver 8080

### Serveur accessible sur tout le réseau

- python manage.py runserver 0.0.0.0:8000

## Gestion de la base de données

### Appliquer les migrations

- python manage.py migrate

### Créer les fichiers de migration pour les modifications de modèles

- python manage.py makemigrations

### Afficher l’état des migrations

- python manage.py showmigrations

### Accéder directement à la base via le shell (dbshell)

- python manage.py dbshell

### Créer un superutilisateur (pour l’admin)

- python manage.py createsuperuser

## Shell et tests

### Lancer le shell interactif Django

- python manage.py shell

### Lancer les tests

- python manage.py test

## Autres commandes utiles

### Vérifier la configuration du projet

- python manage.py check

### Afficher les URL du projet

- python manage.py show_urls

### Faire un dump de la base de données

- python manage.py dumpdata > data.json

### Charger un dump dans la base

- python manage.py loaddata data.json

##  Commandes pour le développement

### Créer un superutilisateur

- python manage.py createsuperuser

### Lancer le serveur avec debug activé (mode développement) :

- python manage.py runserver --settings=nom_du_projet.settings

### Générer des fichiers statiques

- python manage.py collectstatic