from .models import Article, UserFavouriteArticle
from django.views.generic import ListView,  DetailView, CreateView
from django.urls import reverse_lazy
from .forms import ArticleForm
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponse

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
    login_url = "/login/"

    def get_queryset(self):
        user = self.request.user
        return Article.objects.filter(author=user).order_by('-created')

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = "articles/publish.html"
    success_url = reverse_lazy("articles:articles-list")
    login_url = "/login/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class FavouritesListView(LoginRequiredMixin, ListView):

    model = UserFavouriteArticle
    template_name = "articles/favourites.html"
    context_object_name = "favourites"
    login_url = "/login/"

    def get_queryset(self):
        return UserFavouriteArticle.objects.filter(user=self.request.user)
    

class ArticleDetailView(DetailView):
    
    model = Article
    template_name = "articles/detail.html"
    context_object_name = "article"
    ordering = ['-created']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['already_fav'] = False
        if user.is_authenticated:
            context['already_fav'] = UserFavouriteArticle.objects.filter(user=user, article=self.object).exists()
        return context

class FavouritesCreateView(LoginRequiredMixin, CreateView):
    model = UserFavouriteArticle
    fields = []
    login_url = '/login/'
    template_name = "articles/favourites.html"
    # context_object_name = "article"

    def form_valid(self, form):
        user = self.request.user
        article = Article.objects.get(pk=self.kwargs["pk"])

        fav_exists = UserFavouriteArticle.objects.filter(
            user=self.request.user,
            article=article
        ).exists()

        if fav_exists:
            return HttpResponse("Déjà en favori", status=409)

        form.instance.user = self.request.user
        form.instance.article = Article.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
     
    def get_success_url(self):
        return reverse_lazy("articles:article-detail", kwargs={"pk": self.kwargs["pk"]})