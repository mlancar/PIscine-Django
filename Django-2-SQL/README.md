# CREER UNE DATABASE

## 1. Installer PostgreSQL et psycopg2  
## 2. Configurer PostgreSQL dans settings.py  
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nom_de_ta_base',   # ex : mydb
        'USER': 'ton_user',         # ex : postgres
        'PASSWORD': 'ton_mot_de_passe',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
## 3. Créer une app si ce n’est pas déjà fait  
    python manage.py startapp ex00

## 4. Définir un modèle Django (= table SQL)  
Dans ex00/models.py :

```
from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    date_pub = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.titre
```
Ici Article = table SQL ex00_article (Django préfixe avec le nom de l’app par défaut).

## 5. Créer la table en base  
```shell
docker-compose run django python manage.py makemigrations
docker-compose run django python manage.py migrate
```
## 6. Vérifier avec Django shell  
```shell
python manage.py shell
```

```
from ex00.models import Article

a = Article.objects.create(titre="Hello", contenu="Ceci est un test")
print(a.id)  # → l’ID de ton enregistrement
```

Django a créé la table ex00_article dans PostgreSQL.

Tu peux interagir avec elle via l’ORM.

