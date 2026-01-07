from django.db import models

# Create your models here.
class Produit(models.Model):
    ingredient = models.TextField()
    
    def __str__(self):
        return self.ingredient