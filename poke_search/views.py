from django.shortcuts import render

from .functions import get_pokemon_list

# Create your views here.

def home(request):
    search_name = ''
    pokemon_list = []

    if 'search_name' in request.GET:
        search_name = request.GET['search_name'].lower().strip()
        pokemon_list = get_pokemon_list(search_name)

    context = {
        'search_name': search_name,
        'pokemon_list': pokemon_list,
    }
    return render(request, 'poke_search/home.html', context)