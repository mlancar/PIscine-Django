from django.shortcuts import render

from django.shortcuts import HttpResponse
from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.db.utils import ProgrammingError
from .models import People, Planets
import os
import json

# Create your views here.

def display(request):
    try:
        people_dic = []

        people = People.objects.all()
        planets = Planets.objects.all()

        people_dic = []
        for p, planet in zip(people, planets):
            # climate = p.climate
            people_dic.append({
                'name': p.name,
                'homeworld': p.homeworld,
                'climate': planet.climate
                }
            )
        sorted_people = sorted(people_dic, key=lambda x: x["name"])
        context = {'people' : sorted_people}
        return render(request, 'ex09/display.html', context)
    except ProgrammingError as e:
        return HttpResponse("No data available")
