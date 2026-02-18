from django.shortcuts import render
from .models import Article
from django.views.generic import ListView

# Create your views here.

class ArticleListView(ListView):

    model = Article
    template_name = "articles/list.html"
    context_object_name = "articles"
    ordering = ['-created']