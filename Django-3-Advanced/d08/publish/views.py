from django.views.generic import CreateView
from django.urls import reverse_lazy
from articles.models import Article
from .forms import ArticleForm

# Create your views here.

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "publish/publish.html"
    success_url = reverse_lazy("articles:list")