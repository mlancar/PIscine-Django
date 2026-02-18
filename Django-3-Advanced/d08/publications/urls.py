from django.urls import path
from .views import UserArticleListView

urlpatterns = [
    path('', UserArticleListView.as_view(), name='user-articles')
]
