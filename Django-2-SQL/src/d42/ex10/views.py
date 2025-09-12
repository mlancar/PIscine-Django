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
            selected = form.cleaned_data['min_date']
            if selected == "":
                success = False
            else:
                success = True
                
        else:
            success = False
            form = MyForm()
            # form.fields['title'].choices = choices
        return render(request, 'ex10/form.html', {'form': form, "success": success})
    except ProgrammingError as e:
        return HttpResponse("No data available")

