from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:code>/", views.produit_detail, name="produit_detail"),
]