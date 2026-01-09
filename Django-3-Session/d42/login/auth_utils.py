from django.conf import settings

def authenticate_user(username, password):
    return getattr(settings, "USERS_DB", {}).get(username) == password