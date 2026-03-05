from django.urls import path, include
from .views import ArticleListView, FavouritesCreateView, ArticleDetailView, UserArticleListView, ArticleCreateView, FavouritesListView

app_name = "articles"

urlpatterns = [
    path('', ArticleListView.as_view(), name='articles-list'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('<int:pk>/add-favourite/', FavouritesCreateView.as_view(), name='add-favourite'),
    path('publications/', UserArticleListView.as_view(), name='user-publications'),
    path('publish/', ArticleCreateView.as_view(), name='publish-articles'),
    path('favourites/', FavouritesListView.as_view(), name='favourites-list'),

]
