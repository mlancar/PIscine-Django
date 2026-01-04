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
        if not People.objects.exists():
            raise ValueError("No data available, please use the following command line before use: docker-compose run django python manage.py loaddata ex10/fixtures/ex10_initial_data.json")
        if not Planets.objects.exists():
            raise ValueError("No data available, please use the following command line before use: docker-compose run django python manage.py loaddata ex10/fixtures/ex10_initial_data.json")
        form = MyForm(request.POST)
        if form.is_valid():
            min_date = form.cleaned_data['min_date']
            max_date = form.cleaned_data['max_date']
            diameter = form.cleaned_data['diameter']
            char_gender = form.cleaned_data['gender']
            if min_date == "":
                success = False
            else:
                success = True
                matching_characters = People.objects.filter(
                    gender=char_gender,
                    homeworld__diameter__gte=diameter
                )
                movie_list  =  Movies.objects.filter(
                    release_date__gt=min_date,
                    release_date__lt=max_date,
                    characters__in=matching_characters
                    ).prefetch_related(
                        Prefetch("characters", queryset=matching_characters)
                    ).distinct()
                movies_dict = []
                for movie in movie_list:
                     for c in movie.characters.all():
                        movies_dict.append({
                            "title": movie.title,
                            "characters": c.name,
                            "gender": c.gender,
                            "planet": c.homeworld.name,
                            "diameter": c.homeworld.diameter

                        })
                if not movies_dict:
                    raise ValueError("Nothing corresponding to your research")
                context = {'movies' : movies_dict}
                return render(request, 'ex10/display.html', context)
        else:
            success = False
            form = MyForm()
        return render(request, 'ex10/form.html', {'form': form, "success": success})
    except (ProgrammingError, ValueError) as e:
        return HttpResponse(e)

