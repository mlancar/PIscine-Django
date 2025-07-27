from django.shortcuts import render
from .forms import MyForm
import logging

#j'utilse pas basic_config parce que j'avais des message de log sur server django
#donc je configure mon fichier de log moi meme

logger = logging.getLogger('form_logger') #pas dee conflit avec django
handler = logging.FileHandler('data.log') 
formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def form_page(request):
    # if request.method == 'POST':
    print("TEST")
    form = MyForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        age = form.cleaned_data['age']
        email = form.cleaned_data['email']

        logger.info(f"name: {name} | age: {age} | email: {email}")

        context = {
            'form': form,
            'success': True,
            'name': name,
            'age': age,
            'email': email
        }
        return form
    else:
        form = MyForm()
    return form 

def display_historic():
    try:
        with open("data.log", "r") as f:
            print("teST LA")
            return f.readlines()[::-1] #[::-1] inverse l'ordre d'affichage, du plus recenet au plus ancien
    except FileNotFoundError:
        return []

def init_component(request):
    form = form_page(request)
    historic = display_historic()

    return render(request, 'ex02/index.html', {
        'form': form,
        'historic': historic
        })

# TEMPLATE DJANGO
# {% for item in liste %}
#     {{ item }}
# {% empty %}
#     Aucune donnée
# {% endfor %}

# EQUIVALENT PYTHON 
# if liste:
#     for item in liste:
#         print(item)
# else:
#     print("Aucune donnée")
