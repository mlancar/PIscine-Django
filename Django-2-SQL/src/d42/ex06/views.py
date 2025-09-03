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
        cur = connection.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS ex06_movies (
                title VARCHAR(64) UNIQUE NOT NULL,
                episode_nb SERIAL PRIMARY KEY,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_Date DATE NOT NULL,
                created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """)
        connection.commit()
        cur.execute("""
            CREATE OR REPLACE FUNCTION update_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
            NEW.updated = now();
            NEW.created = OLD.created;
            RETURN NEW;
            END;
            $$ language 'plpgsql';
            CREATE TRIGGER update_films_changetimestamp BEFORE UPDATE
            ON ex06_movies FOR EACH ROW EXECUTE PROCEDURE
            update_changetimestamp_column();
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
        cur = connection.cursor()
        context = []
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
            cur.execute("SELECT * FROM ex06_movies WHERE title = %s;", (movie[0],))
            if cur.fetchone() is not None:
                context.append(f"Error: {movie[0]} already exists")
                continue;
            cur.execute("SELECT * FROM ex06_movies WHERE episode_nb = %s;", (movie[1],))
            if cur.fetchone() is not None:
                context.append(f"Error: {movie[0]} {movie[1]} already exists")
                continue;
            context.append("OK")
            cur.execute("""
                INSERT INTO ex06_movies (title, episode_nb, opening_crawl, director, producer, release_date)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (movie[0], movie[1], movie[2], movie[3], movie[4], movie[5]))
        connection.commit()
        cur.close()
        connection.close()
    
    except Error as e:
        return HttpResponse(f"No data available")
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
        cur.execute("SELECT * FROM ex06_movies")
        conn.commit()
        movies = cur.fetchall()
        cur.close()
        conn.close()
        if not movies:
            raise ValueError("No data available")
        movies_dic = []
        print("HELLLOOOO")
        for movie in movies:
            print(f"movie = {movie}")
            movies_dic.append({
                'title': movie[0],
                'episode_nb': movie[1],
                'opening_crawl': movie[2],
                'director': movie[3],
                'producer': movie[4],
                'release_date': movie[5],
                'created': movie[6],
                'updated': movie[7]
                }
            )
        context = {'movies': movies_dic}
        
        return render(request, 'ex06/display.html', context)
    except Exception as e:
        return HttpResponse(f"No data available")

def update(request):
    try:
        conn = psycopg2.connect(
            dbname=settings.DATABASES['default']['NAME'],
            user=settings.DATABASES['default']['USER'],
            password=settings.DATABASES['default']['PASSWORD'],
            host=settings.DATABASES['default']['HOST'],
            port=settings.DATABASES['default']['PORT']
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM ex06_movies")
        conn.commit()
        movies = cur.fetchall()
        
        choices = []
        choices = [('', '---Select a movie---')]
        for i, movie in enumerate(movies, start=1):
            choices.append(
                (movie[0], movie[0])
            )
        form = MyForm(request.POST)
        form.fields['title'].choices = choices
        if form.is_valid():
            opening_crawl = form.cleaned_data['text']
            title = form.cleaned_data['title']
            if opening_crawl == "":
                success = False
            else:
                success = True
                cur.execute("""
                    UPDATE ex06_movies
                    SET opening_crawl = %s
                    WHERE title = %s;""",
                    (opening_crawl, title,))
                cur.execute("""SELECT title, created, updated
                            FROM ex06_movies
                            WHERE title = 'The Phantom Menace';""")
                conn.commit()
        else:
            success = False
            form = MyForm()
            form.fields['title'].choices = choices
        
        cur.close()
        conn.close()
    except Error as e:
        return HttpResponse(f"No data available")
    return render(request, 'ex06/update.html', {'form': form, "success": success})
