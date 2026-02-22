from django.urls import path
from .views import ArticleListView, FavouritesCreateView, ArticleDetailView

app_name = "articles"

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles-list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:pk>/add-favourite/', FavouritesCreateView.as_view(), name='add-favourite')
   
]
