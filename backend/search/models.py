from django.db import models
from django.contrib.auth.models import User

# Table Produit
class Produit(models.Model):
    nom = models.CharField(max_length=255, default='Produit inconnu')
    ingredient = models.TextField()
    nutriscore = models.CharField(max_length=1, default='D')  # A, B, C, D, E
    categorie = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.nom

# Table pour enregistrer les produits de base et leur remplacement pour un utilisateur
class Favori(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    produit_de_base = models.ForeignKey(Produit, related_name='base', on_delete=models.CASCADE)
    produit_remplacement = models.ForeignKey(Produit, related_name='remplacement', on_delete=models.CASCADE)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.utilisateur.username}: {self.produit_de_base.nom} → {self.produit_remplacement.nom}"