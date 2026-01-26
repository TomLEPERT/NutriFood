from django.test import TestCase
from django.urls import reverse
from .models import Produit

class ProduitModelTests(TestCase):
    def test_create_produit(self):
        p = Produit.objects.create(
            nom="Eau Test",
            nutriscore="A",
            categorie="Boissons,Eaux",
            ingredient="eau"
        )
        self.assertEqual(Produit.objects.count(), 1)
        self.assertEqual(p.nom, "Eau Test")
        self.assertEqual(p.nutriscore, "A")

    def test_str_returns_name(self):
        p = Produit.objects.create(nom="Produit X", nutriscore="C", categorie="Test")
        self.assertEqual(str(p), "Produit X")


class SearchViewsTests(TestCase):
    def setUp(self):
        # Produit référence
        self.p_ref = Produit.objects.create(
            nom="Eau sucrée",
            nutriscore="D",
            categorie="Boissons,Eaux",
            ingredient="eau, sucre"
        )
        # Substitut meilleur
        self.p_better = Produit.objects.create(
            nom="Eau nature",
            nutriscore="A",
            categorie="Boissons,Eaux",
            ingredient="eau"
        )
        # Produit meilleur mais autre catégorie
        self.p_other_cat = Produit.objects.create(
            nom="Yaourt nature",
            nutriscore="A",
            categorie="Produits laitiers,Yaourts",
            ingredient="lait"
        )

    def test_index_page_status_code_and_template(self):
        url = reverse("search:index")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "search/index.html")

    def test_resultats_without_query(self):
        url = reverse("search:resultats")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Entre un terme")
        self.assertIn("produits", resp.context)

    def test_resultats_with_query_returns_products(self):
        url = reverse("search:resultats")
        resp = self.client.get(url, {"q": "eau"})
        self.assertEqual(resp.status_code, 200)

        produits = resp.context["produits"]
        self.assertTrue(produits.exists())
        self.assertTrue(any("Eau" in p.nom for p in produits))

    def test_resultats_suggests_better_substitute(self):
        """
        On veut que l'algo propose un produit avec un nutriscore meilleur
        (A/B/C mieux que D/E), idéalement même catégorie.
        """
        url = reverse("search:resultats")
        resp = self.client.get(url, {"q": "Eau sucrée"})
        self.assertEqual(resp.status_code, 200)

        produit_reference = resp.context.get("produit_reference")
        meilleur_substitut = resp.context.get("meilleur_substitut")

        self.assertIsNotNone(produit_reference)
        self.assertIsNotNone(meilleur_substitut)

        # vérifie que le substitut est meilleur (A < D)
        self.assertEqual(produit_reference.nutriscore, "D")
        self.assertIn(meilleur_substitut.nutriscore, ["A", "B", "C"])

        # vérifie qu'il privilégie la même catégorie
        self.assertIn("Boissons", meilleur_substitut.categorie)

    def test_produit_detail_200(self):
        url = reverse("search:produit_detail", args=[self.p_ref.id])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "search/produit_detail.html")
        self.assertContains(resp, self.p_ref.nom)

    def test_produit_detail_404_if_not_found(self):
        url = reverse("search:produit_detail", args=[999999])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)