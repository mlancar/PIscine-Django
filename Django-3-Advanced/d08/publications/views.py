from django.views.generic import ListView
from articles.models import Article

# Create your views here.

class UserArticleListView(ListView):
    model = Article
    template_name = "publications/publications.html"
    context_object_name = "articles"

    def get_queryset(self):
        user = self.request.user
        return Article.objects.filter(author=user).order_by('-created')