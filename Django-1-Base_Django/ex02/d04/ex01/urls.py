from django.urls import path
from . import views

urlpatterns = [
    path("django/", views.django_page),
    path("affichage/", views.affichage_page),
    path("templates/", views.templates_page),

]