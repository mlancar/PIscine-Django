from django.shortcuts import render
from .forms import MyForm
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.db.utils import ProgrammingError
from .models import People, Planets, Movies
from django.db.models import Prefetch

# Create your views here.

def form(request):
    try:

        movies = Movies.objects.all()
        planet = Planets.objects.all()
        

        form = MyForm(request.POST)
        # form.fields['movies minimum release data'].choices = min_data
        if form.is_valid():
            min_date = form.cleaned_data['min_date']
            max_date = form.cleaned_data['max_date']
            diameter = form.cleaned_data['diameter']
            char_gender = form.cleaned_data['gender']
            if min_date == "":
                success = False
            else:
                success = True
                print(min_date)
                print(max_date)
                print(diameter)
                print(char_gender)
                matching_characters = People.objects.filter(
                    gender=char_gender,
                    homeworld__diameter__gte=diameter
                )
                print("Matching characters:", matching_characters.count())
                movie_list  =  Movies.objects.filter(
                    release_date__gt=min_date,
                    release_date__lt=max_date,
                    characters__in=matching_characters
                    ).prefetch_related(
                        Prefetch("characters", queryset=matching_characters)
                    ).distinct()
                movies_dict = []
                print("Nombre de films :", len(movie_list))
                for movie in movie_list:
                     for c in movie.characters.all():
                        movies_dict.append({
                            "title": movie.title,
                            "characters": c.name,
                            "gender": c.gender,
                            "planet": c.homeworld.name,
                            "diameter": c.homeworld.diameter

                        })

                for movie in movies_dict:
                    print(f"TITLE = {movie['title']}")
                context = {'movies' : movies_dict}
                return render(request, 'ex10/display.html', context)
                # search_planets = Planets.objects.filter(diameter__gt=diameter)

        else:
            success = False
            form = MyForm()
            # form.fields['title'].choices = choices
        return render(request, 'ex10/form.html', {'form': form, "success": success})
    except ProgrammingError as e:
        return HttpResponse("No data available")

