from django.shortcuts import render
from django.shortcuts import HttpResponse
import psycopg2
from psycopg2 import sql, OperationalError, Error
from django.conf import settings
from pathlib import Path
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
                homeworld VARCHAR(64),
                FOREIGN KEY (homeworld) REFERENCES ex08_planets(name)
                )    
                """)
        connection.commit()
        cur.close()
        connection.close()
        
        return HttpResponse("OK")
    except Error as e:
        return HttpResponse(f"No data available")
    
    except Error as e:
        return HttpResponse(f"Error SQL : {e}")

#FAUDRA DIVISER CETTE FONCTION LA C"EST PAS POSSIBLE LA

def populate_people(connection, cur, context):

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
        except UndefinedTable as e:
            transaction.rollback()
            # context.append(f"Error: Database people does not exist")
            # context.append
            return HttpResponse(e)
            #return dans la fonction comme ca onfait pas la suite
        id = 1
        for id, people in enumerate(people_list):
            cur.execute("""
                INSERT INTO ex08_people (id, name, climate, diameter, orbital_period, population, rotation_period, surface_water, terrain)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (id, people[0], people[1], people[2], people[3], people[4], people[5], people[6], people[7]))
        context.append("OK")
        connection.commit()
        return context
    except Error as e:
        context.append(e)
        return context
        # context.append(f"Error: People ID: {id} already exists")
    return context

def populate_planets(connection, cur, context):

    csv_path = os.path.join(os.path.dirname(__file__), 'ressources' , 'planets.csv')
    try:
        with open(csv_path, "r") as file:
            list_file = file.read()
    except Error as e:
        return HttpResponse(f"No data available")
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
        except :
            context.append(f"Error: Database planet does not exist")

            #return dans la fonction comme ca on fait pas la suite
        for id, planet in enumerate(planets):
            cur.execute("""
                INSERT INTO ex08_planets (id, name, climate, diameter, orbital_period, population, rotation_period, surface_water, terrain)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);
            """, (id, planet[0], planet[1], planet[2], planet[3], planet[4], planet[5], planet[6], planet[7]))
        connection.commit()
        context.append("OK")
        return context 
    except Error as e:
        context.append(e)
        return context
        # context.append(f"Error: Planet ID: {id} already exists")


def populate(request):

    connection = psycopg2.connect(
        dbname=settings.DATABASES['default']['NAME'],
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        host=settings.DATABASES['default']['HOST'],
        port=settings.DATABASES['default']['PORT']
    )
    cur = connection.cursor()
    # try:
    #     cur.copy_from(file, "ex08_planets", null="NULL", sep="\n")
    #     connection.commit()
    # except Error as e:
    #     return HttpResponse(e)

    context = []
    
    context = populate_planets(connection, cur, context)
    context = populate_people(connection, cur, context)
    
    cur.close()
    connection.close()
    
    return HttpResponse(context)
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
        # if not planets:
        #     raise ValueError("No data available")
        planets_dic = []
        # for planet in planets:
        #     planets_dic.append({
        #         'title': planet[0],
        #         'episode_nb': planet[1],
        #         'opening_crawl': planet[2],
        #         'director': planet[3],
        #         'producer': planet[4],
        #         'release_date': planet[5],
        #         'created': planet[6],
        #         'updated': planet[7]
        #         }
        #     )
        
        # context = {'movies': planets_dic}

        people = cur.fetchall()
        # if not people:
        #     raise ValueError("No data available")
        people_dic = []
        for p in people:
            print("HELLLOOOO")
            print(f"TEST {p}")
            climate = p[8]
            people_dic.append({
                'name': p[1],
                'homeworld': p[8],
                'climate': planets[climate]
                }
            )
        context = {'people' : people_dic}
        print("TEST ")

        # for p in context:
            # print(f"CONTEXT = {p[0]}")
        cur.close()
        conn.close()
        return render(request, 'ex08/display.html', context)
    except Error as e:
        return HttpResponse(e)
        return HttpResponse(f"No data available")