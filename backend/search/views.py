from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from .models import Produit

def index(request):
    return HttpResponse("Home OK. Teste /<id>/ (ex: /1/)")

def produit_detail(request, code):
    produit = get_object_or_404(Produit, pk=code)
    return render(request, "search/produit_detail.html", {"produit": produit})