from django.shortcuts import render
from .forms import MyForm
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.db.utils import ProgrammingError
from .models import People, Planets, Movies

# Create your views here.

def form(request):
    try:

        movies = Movies.objects.all()
        planet = Planets.objects.all()
        

        form = MyForm(request.POST)
        # form.fields['movies minimum release data'].choices = min_data
        if form.is_valid():
            min_date = form.cleaned_data['min_date']
            max_date = form.cleaned_data['max_date']
            diameter = form.cleaned_data['diameter']
            char_gender = form.cleaned_data['gender']
            if min_date == "":
                success = False
            else:
                success = True
                print(min_date)
                print(max_date)
                print(diameter)
                print(char_gender)
                people = People.objects.all()
                planets = Planets.objects.all()

                person_list = list(People.objects.filter(gender=char_gender))
                movie_list  = list(Movies.objects.filter(release_date__gt=min_date, release_date__lt=max_date))

                search_dic = []

                for person in person_list:
                    Movies.objects.filter(characters=person)
                   

                if planet.diameter > diameter:
                        search_dic.append(planet.diameter)

        else:
            success = False
            form = MyForm()
            # form.fields['title'].choices = choices
        return render(request, 'ex10/form.html', {'form': form, "success": success})
    except ProgrammingError as e:
        return HttpResponse("No data available")

