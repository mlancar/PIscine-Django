from django.views.generic import CreateView
from django.urls import reverse_lazy
from articles.models import Article
from .forms import ArticleForm

# Create your views here.

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "publish/publish.html"
    success_url = reverse_lazy("articles-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
# je dois mettre publish dans lapp publication. Pas creer une nouvelle app. 
# donc supp cette app