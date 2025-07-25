from django.shortcuts import render
from .forms import MyForm

def form_page(request):
    # if request.method == 'POST':
    form = MyForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        age = form.cleaned_data['age']
        email = form.cleaned_data['email']
        return render(request, 'ex02/index.html', {
            'form': form,
            'success': True,
            'name': name,
            'age': age,
            'email': email
        })
    else:
        form = MyForm()

    return render(request, 'ex02/index.html', {'form': form})