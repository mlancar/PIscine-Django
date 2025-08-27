from django.shortcuts import HttpResponse
import psycopg2
from psycopg2 import sql, OperationalError, Error
from django.conf import settings

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
            CREATE TABLE IF NOT EXISTS ex00_movies (
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