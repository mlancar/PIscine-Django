from django.conf import settings
import sys

def create_user(username, password):
    if not hasattr(settings, "USERS_DB"):
        settings.USERS_DB = {}  # <- assure-toi que le dictionnaire existe
    if username in settings.USERS_DB:
        return False
    settings.USERS_DB[username] = password
    return True