from django.views.generic import DetailView
from articles.models import Article

# Create your views here.

class ArticleDetailView(DetailView):
    
    model = Article
    template_name = "detail/detail.html"
    context_object_name = "article"
    ordering = ['-created']