from django.shortcuts import render

def make_gradient(start, end, steps):
    
    colors = []
    for i in range(steps):
        colors.append(
            "#{:02x}{:02x}{:02x}".format( #x convertir en hexa, 02 sur 2 caractere, : pour dire c'est du formatage
                int(start[0] + (end[0]-start[0])*i/(steps-1)),
                int(start[1] + (end[1]-start[1])*i/(steps-1)),
                int(start[2] + (end[2]-start[2])*i/(steps-1))
            )
        )
    return colors


def init_component(request):

    rows = 51
    columns = 4
    black_gradient = make_gradient((0,0,0), (255,255,255), rows)
    red_gradient = make_gradient((200,0,0), (255,255,255), rows)
    blue_gradient = make_gradient((0,0,200), (255,255,255), rows)
    green_gradient = make_gradient((0,200,0), (255,255,255), rows)
    
    gradient_colors = [black_gradient, red_gradient, green_gradient, blue_gradient]
    colored_rows = []

    for i in range(rows):
        colors = [black_gradient[i], red_gradient[i], green_gradient[i], blue_gradient[i]]
        colored_rows.append(colors)

    context = {
        'rows': colored_rows,
        'columns': range(columns),
        # # 'black': black
        # 'black': black
    }
    return render(request, 'ex03/index.html', context)
