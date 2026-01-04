
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
docker system prune -a --volumes

```
## DELETE CONTAINERS
```
docker rm -f $(docker ps -aq)
```
## DELETE IMAGES
```
docker rmi -f $(docker images -q)
```
## DELETE VOLUMES
```
docker volume rm $(docker volume ls -q)
```
## ENTER DATABSE  
```
docker-compose run django python manage.py dbshell
```
## DELETE TABLE  
```
TRUNCATE TABLE <table> RESTART IDENTITY;
```
## EXECUTE SQL CMD IN DJANGO  
```
cur.execute("command")
conn.commit()
```
- with an extern variable  
```
 cur.execute("CMD var = %s;", (var_extern,))
 ```