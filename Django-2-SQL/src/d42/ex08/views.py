from django.shortcuts import render
from django.shortcuts import HttpResponse
import psycopg2
from psycopg2 import sql, OperationalError, Error
from django.conf import settings
from pathlib import Path
import os

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
                homeworld VARCHAR(64),
                FOREIGN KEY (homeworld) REFERENCES ex08_planets(name)
                )    
                """)
        connection.commit()
        cur.close()
        connection.close()
        
        return HttpResponse("OK")
    except Error as e:
        return HttpResponse(e)
        return HttpResponse(f"No data available")
    
    except Error as e:
        return HttpResponse(f"Error SQL : {e}")

#FAUDRA DIVISER CETTE FONCTION LA C"EST PAS POSSIBLE LA
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
    except Error as e:
        return HttpResponse(f"No data available")
    
    #FONCTION PLANETS
    context = []
    csv_path = os.path.join(os.path.dirname(__file__), 'ressources' , 'planets.csv')
    try:
        with open(csv_path, "r") as file:
            list_file = file.read()
    except Error as e:
        return HttpResponse(f"No data available")

    context = []
    planets= []

    for line in list_file.strip().split("\n"):
        list_elem = [] #declarer dans la boucle 
        for element in line.strip().split("\t"):
            if element == "NULL": #sinon ca ecrit "NULL" directement
                list_elem.append(None)
            else:
                list_elem.append(element)
        planets.append(list_elem)

    try:
        id = 1
        try:
            cur.execute("SELECT * FROM ex08_planets;")
        except:
            context.append(f"Error: Database planet does not exist")
            #return dans la fonction comme ca on fait pas la suite
        for id, planet in enumerate(planets):
            cur.execute("SELECT * FROM ex08_planets WHERE id = %s;", (planet[0],))
            cur.execute("SELECT * FROM ex08_planets WHERE name = %s;", (planet[1],))
            cur.execute("""
                INSERT INTO ex08_planets (id, name, climate, diameter, orbital_period, population, rotation_period, surface_water, terrain)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (id, planet[0], planet[1], planet[2], planet[3], planet[4], planet[5], planet[6], planet[7]))
        connection.commit()
        context.append("OK")
       
    except Error as e:
        context.append(f"Error: Planet ID: {id} already exists")
    
    #FONCTION PEOPLE

    csv_path = os.path.join(os.path.dirname(__file__), 'ressources' , 'people.csv')
    try:
        with open(csv_path, "r") as file:
            list_file = file.read()
    except Error as e:
        return HttpResponse(f"No data available")
    
    people_list = []
    for line in list_file.strip().split("\n"):
        list_elem = [] #declarer dans la boucle 
        for element in line.strip().split("\t"):
            if element == "NULL": #sinon ca ecrit "NULL" directement
                list_elem.append(None)
            else:
                list_elem.append(element)
        people_list.append(list_elem)
    try:
        try:
            cur.execute("SELECT * FROM ex08_people;")
        except:
            context.append(f"Error: Database people does not exist")
            #return dans la fonction comme ca onfait pas la suite
        id = 1
        for id, people in enumerate(people_list):
            cur.execute("SELECT * FROM ex08_people WHERE id = %s;", (people[0],))
            cur.execute("SELECT * FROM ex08_people WHERE name = %s;", (people[1],))
            cur.execute("""
                INSERT INTO ex08_people (id, name, climate, diameter, orbital_period, population, rotation_period, surface_water, terrain)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (id, people[0], people[1], people[2], people[3], people[4], people[5], planet[6], planet[7]))
        context.append("OK")
    except Error as e:
        context.append(f"Error: People ID: {id} already exists")
    connection.commit()
    cur.close()
    connection.close()
    return HttpResponse("<br>".join(context))
