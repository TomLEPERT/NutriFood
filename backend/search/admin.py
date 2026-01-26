from django.contrib import admin
from .models import Produit

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ('nom', 'nutriscore', 'categorie')  # colonnes visibles
    search_fields = ('nom', 'categorie')
    list_per_page = 50
