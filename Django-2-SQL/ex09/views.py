from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import People, Planets

# Create your views here.

def display(request):
    try:
        if not People.objects.exists():
            raise ValueError("No data available, please use the following command line before use: docker-compose run django python manage.py loaddata ex09/fixtures/ex09_initial_data.json")
        if not Planets.objects.exists():
            raise ValueError("No data available, please use the following command line before use: docker-compose run django python manage.py loaddata ex09/fixtures/ex09_initial_data.json")
        people = People.objects.all()
        planets = Planets.objects.all()
        people_dic = []
        for p, planet in zip(people, planets):
            if p.homeworld is not None:
                homeworld = p.homeworld.name
            if planet.climate is not None and ("windy" in planet.climate or "moderately" in planet.climate):
                people_dic.append({
                    'name': p.name,
                    'homeworld': homeworld,
                    'climate': planet.climate,
                    }
                )
        sorted_people = sorted(people_dic, key=lambda x: x["name"])
        context = {'people' : sorted_people}
        return render(request, 'ex09/display.html', context)
    except ValueError as e:
        return HttpResponse(e)
