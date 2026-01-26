from django.urls import path
from . import views

app_name = "search"

urlpatterns = [
    path("", views.index, name="index"),
    path("resultats/", views.resultats, name="resultats"),
    path("<int:code>/", views.produit_detail, name="produit_detail"),
]