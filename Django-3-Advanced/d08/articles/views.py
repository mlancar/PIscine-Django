from .models import Article, UserFavouriteArticle
from django.views.generic import ListView,  DetailView, CreateView
from django.urls import reverse_lazy
from .forms import ArticleForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ArticleListView(ListView):

    model = Article
    template_name = "articles/list.html"
    context_object_name = "articles"
    ordering = ['-created']


class UserArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "articles/publications.html"
    context_object_name = "articles"

    def get_queryset(self):
        user = self.request.user
        return Article.objects.filter(author=user).order_by('-created')

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "articles/publish.html"
    success_url = reverse_lazy("articles-list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class FavouritesListView(LoginRequiredMixin, ListView):

    model = UserFavouriteArticle
    template_name = "articles/favourites.html"
    context_object_name = "favourites"

    def get_queryset(self):
        return UserFavouriteArticle.objects.filter(user=self.request.user)
    

class ArticleDetailView(DetailView):
    
    model = Article
    template_name = "articles/detail.html"
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