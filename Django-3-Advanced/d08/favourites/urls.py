from django.urls import path
from .views import FavouritesListView

urlpatterns = [
    path('', FavouritesListView.as_view(), name='favourites-list')
]