from django.shortcuts import render

def django_page(request):
    return render(request, 'ex01/django.html')

def affichage_page(request):
    return render(request, 'ex01/affichage.html')

def templates_page(request):
    return render(request, 'ex01/templates.html')

def home_page(request):
    return render(request, 'ex01/home.html')