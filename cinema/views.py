from django.shortcuts import render
from unicodedata import name
from cinema.models import Categorie, Films, Ticket, Utilisateur, Salle, Place
from django.views import generic

# Create your views here.

def cine(request, *arg, **kwarg):
    films = Films.objects.all()
    categorie = Categorie .objects .all()
    context = {
        'films' : films
    }

    # context['films'] = films
    context['categorie'] = categorie

    return render(request, 'cinema/index.html', context)


def films(request, *arg, **kwarg):
    films = Films.objects.all()
    categorie = Categorie .objects .all()
    context = {
        'films' : films
    }


    # context['films'] = films
    context['categorie'] = categorie

    return render(request, 'cinema/films_list.html', context)    


def reservations(request, *arg, **kwarg):
    context = {}
    return render(request, 'cinema/reservations.html', context)      

def news(request, *arg, **kwarg):
    
    films = Films.objects.all()
    categorie = Categorie .objects .all()
    context = {
        'films' : films
    }

    # context['films'] = films
    context['categorie'] = categorie

    return render(request, 'cinema/new.html', context)



def filmsDetail(request, idfilm):
    film = None
    try:
        film = Films.objects.get(pk=idfilm) 
       
    except Films.DoesNotExist:
        raise  http404('Films does not exist') 
    
    return render(request, 'cinema/detail_film.html', context={'film': film})

class FilmsDetailView(generic.DetailView):
     model = Films
    # context_object_name = 'films'
    # queryset = Films.objects.all()
    # films = Films.objects.get(pk=primary_key) 
    # queryset = Films.objects.filter(titre__icontains='loup'[:2])
    # template_name = 'fimls/detail_list.html'

class FilmsListView(generic.ListView):

    model = Films
    context_object_name = 'films'
    queryset = Films.objects.all()
    # queryset = Films.objects.filter(titre__icontains='loup'[:2])
    template_name = 'fimls/films_list.html'