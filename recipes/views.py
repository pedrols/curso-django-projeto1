from django.shortcuts import render

# Create your views here.


def home(request):
    # return render(request, 'recipes/home.html')
    # return render(request, 'recipes/home.html', status=201)
    return render(request, 'recipes/home.html', context={
        'name': 'Pedro Lins de Souza',
    })


