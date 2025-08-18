from django.shortcuts import render

def django_page(request):
    return render(request, 'ex01/django.html')

def affichage_page(request):
    return render(request, 'ex01/display.html')

def templates_page(request):
    return render(request, 'ex01/templates.html')
