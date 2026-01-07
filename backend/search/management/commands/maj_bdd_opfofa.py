from django.core.management.base import BaseCommand
import requests
from search.models import Produit

class Command(BaseCommand):
    help = "Met à jour la base de données avec des produits depuis OpenFoodFacts"

    def handle(self, *args, **options):
        categories = ["boissons", "sodas", "biscuits", "fromages", "yaourts"]
        self.stdout.write("Début de la récupération des produits depuis OpenFoodFacts...")

        for cat in categories:
            self.stdout.write(f"Récupération de la catégorie : {cat}")
            url = f"https://world.openfoodfacts.org/category/{cat}.json"
            try:
                response = requests.get(url, params={"page_size": 100})
                response.raise_for_status()
            except requests.RequestException as e:
                self.stdout.write(self.style.WARNING(f"Erreur pour la catégorie {cat} : {e}"))
                continue

            data = response.json()
            products = data.get("products", [])

            for p in products:
                nom = p.get("product_name", "").strip()
                ingredient = p.get("ingredients_text", "").strip()
                nutriscore = p.get("nutriscore_grade", "E")
                categorie_prod = p.get("categories", "").strip()

                # Nettoyer les champs pour éviter les erreurs de longueur
                if nom:
                    nom = nom[:255]  # tronquer le nom si trop long
                    categorie_prod = categorie_prod[:500]  # tronquer la catégorie si trop longue
                    nutriscore = nutriscore[0].upper() if nutriscore else "E"  # garder un seul caractère

                    # Créer ou mettre à jour le produit dans la base
                    Produit.objects.update_or_create(
                        nom=nom,
                        defaults={
                            "ingredient": ingredient,
                            "nutriscore": nutriscore,
                            "categorie": categorie_prod,
                        }
                    )
        self.stdout.write(self.style.SUCCESS("Récupération terminée !"))
