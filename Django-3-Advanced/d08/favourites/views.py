from django.views.generic import ListView
from articles.models import UserFavouriteArticle

# Create your views here.

class FavouritesListView(ListView):

    model = UserFavouriteArticle
    template_name = "favourites/favourites.html"
    context_object_name = "favourites"

    def get_queryset(self):
        return UserFavouriteArticle.objects.filter(user=self.request.user)