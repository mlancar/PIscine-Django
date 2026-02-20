from django.urls import path
from .views import ArticleCreateView

urlpatterns = [
    path('', ArticleCreateView.as_view(), name='publish-articles')
]
