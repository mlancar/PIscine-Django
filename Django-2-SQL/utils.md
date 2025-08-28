
# COMMANDS CHEATSHEET  
## CREATE SITE  
```
django-admin startproject <site>
```
## CREATE APP  
```
python manage.py startapp <app>
```
## MAKEMIGRATION  
```
docker-compose run django python manage.py makemigrations
```
## MIGRATE
```
docker-compose run django python manage.py migrate
```
## BUILD DOCKER  
```
docker-compose up --buil
```
## DELETE VOLUME DATABASE  
```
docker system prune -a
```
## ENTER DATABSE  
```
docker-compose run django python manage.py dbshell
```
## DELETE TABLE  
```
TRUNCATE TABLE <table> RESTART IDENTITY;
```