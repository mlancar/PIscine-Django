create repository
```
mkdir myproject
cd myproject
```
create venv and activate

```
python3 -m venv venv
source venv/bin/ativate
```
install Django

```
pip install django
django-admin startproject mysite .

```
create app
```
python manage.py startapp core
```

it creates a repository core
add core to mysite/settings.py-> INSTALLED_APPS:  
```
INSTALLED_APPS = [
    ...
    'd42.ex00',  # <-- ajoute ton app ici
]
```

## Create a simple page

in core.views.py: 
```
from django.http import HttpResponse

def home(request):
    return render(request, 'core/home.html')
```
in mysite/urls.py:
```
from django.contrib import admin
from django.urls import path
from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
```

## RUN SERVER  
```
python manage.py runserver
```

The server listen to http://127.0.0.1:8000/
On thsi URL you will see "Hello world!"


