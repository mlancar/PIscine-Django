from django.shortcuts import render
from .models import Movies
from django.shortcuts import HttpResponse
from django.core.exceptions import ValidationError
from psycopg2 import sql, Error
from django.shortcuts import render
# Create your views here.

def populate(request):
    
    movies = [
        {"title": "The Phantom Menace", "episode_nb": 1, "opening_crawl": "", "director": "George Lucas", "producer": "Rick McCallum", "release_date": "1999-05-19"},
        {"title": "Attack of the Clones", "episode_nb": 1, "opening_crawl": "", "director": "George Lucas", "producer": "Rick McCallum", "release_date": "2002-05-16"},
        {"title": "Revenge of the Sith", "episode_nb": 3, "opening_crawl": "", "director": "George Lucas", "producer": "Rick McCallum", "release_date": "2005-05-19"},
        {"title": "A New Hope", "episode_nb": 4, "opening_crawl": "", "director": "George Lucas", "producer": "Gary Kurtz, Rick McCallum", "release_date": "1977-05-25"},
        {"title": "The Empire Strikes Back", "episode_nb": 5, "opening_crawl": "", "director": "Irvin Kershner", "producer": "Gary Kurtz, Rick McCallum", "release_date": "1980-05-17"},
        {"title": "Return of the Jedi", "episode_nb": 6, "opening_crawl": "", "director": "Richard Marquand", "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum", "release_date": "1983-05-25"},
        {"title": "The Force Awakens", "episode_nb": 7, "opening_crawl": "", "director": "J. J. Abrams", "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "release_date": "1999-05-19"},   
    ]
    movies = Movies.objects.all()
    if not movies.exists():
        return HttpResponse("No data available")
    context = []
    for movie in movies:
        if Movies.objects.filter(title=movie["title"]).exists():
            context.append(f"Error: {movie['title']} already exists")

        elif Movies.objects.filter(episode_nb=movie["episode_nb"]).exists():
            context.append(f"Error: {movie['title']} episode {movie['episode_nb']} already exists")

        else:
            movie_object = Movies(
                title=movie["title"],
                episode_nb=movie["episode_nb"],
                opening_crawl=movie["opening_crawl"],
                director=movie["director"],
                producer=movie["producer"],
                release_date=movie["release_date"],
            )
            try:
                movie_object.full_clean()
                movie_object.save()
                context.append("OK")

            except ValidationError as e:
                context.append(f"Error: {movie['title']} {e}")
    return HttpResponse("<br>".join(context))

def display(request):
    movies_dic = []
    movies = Movies.objects.all()
    for movie in movies:
        movies_dic.append({
            'title': movie.title,
            'episode_nb': movie.episode_nb,
            'opening_crawl': movie.opening_crawl,
            'director': movie.director,
            'producer': movie.producer,
            'release_date': movie.release_date
            }
        )
    context = {'movies': movies_dic}
    return render(request, 'ex02/index.html', context)
