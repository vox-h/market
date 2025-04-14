from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        'title': 'Main Page',
        'content': 'Главная страница магазина',
        'list': ['first', 'second'],
        'dict': {'first': 1},
        'is_auth': True,
    }

    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse("About site")