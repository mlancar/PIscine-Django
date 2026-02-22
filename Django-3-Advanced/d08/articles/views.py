from .models import Article, UserFavouriteArticle
from django.views.generic import ListView,  DetailView, CreateView
from django.urls import reverse_lazy

# Create your views here.

class ArticleListView(ListView):

    model = Article
    template_name = "articles/list.html"
    context_object_name = "articles"
    ordering = ['-created']

class ArticleDetailView(DetailView):
    
    model = Article
    template_name = "detail/detail.html"
    context_object_name = "article"
    ordering = ['-created']

class FavouritesCreateView(CreateView):
    model = UserFavouriteArticle
    fields = []
    # template_name = "detail/detail.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article = Article.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
     
    def get_success_url(self):
        return reverse_lazy("articles:detail", kwargs={"pk": self.kwargs["pk"]})