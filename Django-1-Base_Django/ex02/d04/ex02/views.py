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
        return render(request, 'ex02/index.html', context)
    else:
        form = MyForm()

    return render(request, 'ex02/index.html', {'form': form})
