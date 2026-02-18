from django.urls import path
from .views import ArticleDetailView

urlpatterns = [
    path('<int:pk>/', ArticleDetailView.as_view(), name='detail')
]
