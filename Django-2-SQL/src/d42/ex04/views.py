from django.shortcuts import HttpResponse
import psycopg2
from psycopg2 import sql, OperationalError, Error
from django.conf import settings
from django.shortcuts import render
from .forms import MyForm

def init(request):
    try:
        connection = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cur =connection.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS ex04_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb SERIAL PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_Date DATE NOT NULL
                )
                """)
        connection.commit()
        cur.close()
        connection.close()
        
        return HttpResponse("OK")
    except OperationalError as e:
        return HttpResponse(f"Error connecting to the Database: {e}")
    
    except Error as e:
        return HttpResponse(f"Error SQL : {e}")

def populate(request):
    try:
        connection = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cur =connection.cursor()
        context = []
        # cur.execute("TRUNCATE TABLE ex04_movies RESTART IDENTITY;")
        movies = [
            ("The Phantom Menace", 1, "", "George Lucas", "Rick McCallum", "1999-05-19"),
            ("Attacks of the Clones",2, "", "George Lucas", "Rick McCallum", "2002-05-16"),
            ("Revenge of the Sith", 3, "", "George Lucas", "Rick McCallum", "2005-05-19"),
            ("A New Hope", 4, "", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-12"),
            ("The Empire Strikes Back", 5, "", "Irvin Kershner", "Gary Kurtz, Rick McCallum", "1980-05-17"),
            ("Return of the Jedi", 6, "", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
            ("The Force Awakens", 7, "", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11"),
        ]


        for movie in movies:
            cur.execute("SELECT * FROM ex04_movies WHERE title = %s;", (movie[0],))
            if cur.fetchone() is not None:
                context.append(f"Error: {movie[0]} already exists")
                continue;
            
            cur.execute("SELECT * FROM ex04_movies WHERE episode_nb = %s;", (movie[1],))
            if cur.fetchone() is not None:
                context.append(f"Error: {movie[0]} {movie[1]} already exists")
                continue;
            context.append("OK")
            cur.execute("""
                INSERT INTO ex04_movies (title, episode_nb, opening_crawl, director, producer, release_date)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (movie[0], movie[1], movie[2], movie[3], movie[4], movie[5]))
        connection.commit()
        cur.close()
        connection.close()
    
    except Error as e:
        # context.append(f"ici Error: {movies[0]} {e}")
        print()
    return HttpResponse("<br>".join(context))


def display(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM ex04_movies")
        movies = cur.fetchall()
        cur.close()
        conn.close()

        movies_dic = []
        for movie in movies:
            movies_dic.append({
                'title': movie[0],
                'episode_nb': movie[1],
                'opening_crawl': movie[2],
                'director': movie[3],
                'producer': movie[4],
                'release_date': movie[5]
                }
            )
        context = {'movies': movies_dic}
        # context = [f"{movie[0]} {movie[1]}: {movie[2]}" for movie in movies]
        return render(request, 'ex02/index.html', context)
    except Exception as e:
        return HttpResponse(f"Error : {e}")

def remove(request):

    form = MyForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']

        context = {
            'form': form,
            'success': True,
            'title': title,
        }
        return form
    else:
        form = MyForm()
    return render(request, 'ex04/index.html', {
        'form': form,
        })
