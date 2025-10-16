from django.shortcuts import HttpResponse
import psycopg2
from psycopg2 import sql, OperationalError, Error
from django.conf import settings
from django.shortcuts import render

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
            CREATE TABLE IF NOT EXISTS ex02_movies (
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
        cur.execute("TRUNCATE TABLE ex02_movies RESTART IDENTITY;")
        movies = [
            ("The Phantom Menace", 1, "", "George Lucas", "Rick McCallum", "1999-05-19"),
            ("Attacks of the Clones", 2, "", "George Lucas", "Rick McCallum", "2002-05-16"),
            ("Revenge of the Sith", 3, "", "George Lucas", "Rick McCallum", "2005-05-19"),
            ("A New Hope", 4, "", "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-12"),
            ("The Empire Strikes Back", 5, "", "Irvin Kershner", "Gary Kurtz, Rick McCallum", "1980-05-17"),
            ("Return of the Jedi", 6, "", "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
            ("The Force Awakens", 7, "", "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11"),
        ]
        context = []
        for movie in movies:
            cur.execute("""
                    INSERT INTO ex02_movies (title, episode_nb, opening_crawl, director, producer, release_date)
                    VALUES (%s, %s, %s, %s, %s, %s)
                """, movie)
            context.append("OK")

        connection.commit()
        cur.close()
        connection.close()

        return HttpResponse("<br>".join(context))
    except OperationalError as e:
        return HttpResponse(f"Error connecting to the Database: {e}")
    
    except Error as e:
        return HttpResponse(f"Error SQL : {e}")

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
        cur.execute("SELECT * FROM ex02_movies")
        movies = cur.fetchall()
        cur.close()
        conn.close()
        if not movies:
            raise ValueError("No data available")
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
        return render(request, 'ex02/index.html', context)
    except Exception as e:
        return HttpResponse(e)
