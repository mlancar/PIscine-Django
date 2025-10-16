from django.shortcuts import render
from django.shortcuts import HttpResponse
import psycopg2
from psycopg2 import Error
from django.conf import settings
import os
from django.db import transaction
from psycopg2.errors import UndefinedTable

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
            CREATE TABLE IF NOT EXISTS ex08_planets (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                climate VARCHAR(128),
                diameter INTEGER,
                orbital_period INTEGER,
                population BIGINT,
                rotation_period INTEGER,
                surface_water REAL,
                terrain VARCHAR(128)
                )
                """)
        connection.commit()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS ex08_people (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                birth_year VARCHAR(32),
                gender VARCHAR(32),
                eye_color VARCHAR(32),
                hair_color VARCHAR(32),
                height INTEGER,
                mass REAL,
                homeworld VARCHAR(64)
                )    
                """)
                # FOREIGN KEY (homeworld) REFERENCES ex08_planets(name)
        connection.commit()
        cur.close()
        connection.close()
        
        return HttpResponse("OK")
    except Error as e:
        return HttpResponse(f"No data available")
    
    except Error as e:
        return HttpResponse(f"Error SQL : {e}")

def populate(request):

    connection = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT']
    )
    cur = connection.cursor()

    csv_path = os.path.join(os.path.dirname(__file__), 'ressources' , 'planets.csv')
    context = []
    try:
        with open(csv_path, "r") as file:
            cur.copy_from(file, "ex08_planets", sep="\t", null="NULL", columns=("name", "climate", "diameter", "orbital_period", "population", "rotation_period", "surface_water", "terrain"))
        connection.commit()
        context.append("OK")
    
    except Error as e:
        return HttpResponse(e)
    
    csv_path = os.path.join(os.path.dirname(__file__), 'ressources' , 'people.csv')
    
    try:
        with open(csv_path, "r") as file:
            cur.copy_from(file, "ex08_people", sep="\t", null="NULL", columns=("name", "birth_year", "gender", "eye_color", "hair_color", "height", "mass", "homeworld"))
        connection.commit()
        context.append("OK")

    except Error as e:
        return HttpResponse(e)
    
    cur.close()
    connection.close()
    
    # return HttpResponse(context)
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
        cur.execute("SELECT * FROM ex08_planets")
        conn.commit()
        planets = cur.fetchall()
        if not planets:
            raise ValueError("No data available")
        cur.execute("SELECT * FROM ex08_people")
        conn.commit()
        people = cur.fetchall()
        if not people:
            raise Error("No data available")
        people_dic = []
        print()
        for p, planet in zip(people, planets):

            if planet[2] is not None and ("windy" in planet[2] or "moderately" in planet[2]):
                people_dic.append({
                    'name': p[1],
                    'homeworld': p[8],
                    'climate': planet[2]
                    }
                )
        sorted_people = sorted(people_dic, key=lambda x: x["name"])
        context = {'people' : sorted_people}
        cur.close()
        conn.close()
        return render(request, 'ex08/display.html', context)
    except Error as e:
        return HttpResponse(e)
        return HttpResponse(f"No data available")