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
## CREATE APP
```
python manage.py startapp core
```

it creates a repository core
add core to mysite/settings.py-> INSTALLED_APPS:  
```
INSTALLED_APPS = [
    ...
    'ex00',  # <-- ajoute ton app ici
]
```
in mysite/urls.py:
```
from django.contrib import admin
from django.urls import path
from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path("core/", include("core.urls")),
]
```
- Add each app created here

## Create a simple page

in core.views.py: 
```
def home(request):
    return render(request, 'core/home.html')
```
- create a url.py in your app  
- path can be  "" or "/something"
```
from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home),
]
```

## RUN SERVER  
```
python manage.py runserver
```

The server listen to http://127.0.0.1:8000/

## ADD TEMPLATE  

- create folders "templates" and "app_name"
- create index.html
- in settings.py add:  




## ADD STATIC/CSS  

- create folders "static" and "css"
- create "style.css"