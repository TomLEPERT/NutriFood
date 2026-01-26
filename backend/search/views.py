from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Produit
from .utils import nutriscore_value

def index(request):
    # page avec formulaire
    return render(request, "search/index.html")

def resultats(request):
    query = (request.GET.get("q") or "").strip()
    produits = Produit.objects.none()
    meilleur_substitut = None
    produit_reference = None

    if query:
        # recherche simple (nom ou catégorie)
        produits = Produit.objects.filter(
            Q(nom__icontains=query) | Q(categorie__icontains=query)
        ).order_by("nom")[:30]

        # on prend le 1er comme "produit de référence"
        produit_reference = produits.first()

        if produit_reference:
            ref_score = nutriscore_value(produit_reference.nutriscore)

            # Candidats: même catégorie (si possible) et nutriscore meilleur
            candidats = Produit.objects.exclude(pk=produit_reference.pk)

            if produit_reference.categorie:
                # "même catégorie" : on cherche une portion de la catégorie
                first_cat = produit_reference.categorie.split(",")[0].strip()
                if first_cat:
                    candidats = candidats.filter(categorie__icontains=first_cat)

            # filtrer sur nutriscore meilleur
            candidats = list(candidats[:300])  # limite pour éviter de charger trop
            meilleurs = [p for p in candidats if nutriscore_value(p.nutriscore) < ref_score]

            # choisir le meilleur: nutriscore le plus bas, puis nom
            meilleurs.sort(key=lambda p: (nutriscore_value(p.nutriscore), p.nom.lower() if p.nom else ""))

            meilleur_substitut = meilleurs[0] if meilleurs else None

    return render(
        request,
        "search/resultats.html",
        {
            "query": query,
            "produits": produits,
            "produit_reference": produit_reference,
            "meilleur_substitut": meilleur_substitut,
        },
    )

def produit_detail(request, code):
    produit = get_object_or_404(Produit, pk=code)
    return render(request, "search/produit_detail.html", {"produit": produit})
