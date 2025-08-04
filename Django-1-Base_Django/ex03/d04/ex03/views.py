from django.shortcuts import render

def init_component(request):

    rows = 51
    columns = 4
    context = {
        'rows': range(rows),
        'columns': range(columns),
    }
    return render(request, 'ex03/index.html', context)
