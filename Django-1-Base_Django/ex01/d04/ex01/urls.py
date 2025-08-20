from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home_page),
    path("django/", views.django_page),
    path("display/", views.display_page),
    path("templates/", views.templates_page),

]