from django.http import HttpResponse
# Create your views here.
from django.template import loader

from movies.models import Movie
from people.models import Person


def index(req):
    latest_movies = Movie.objects.all().order_by('id')
    template = loader.get_template('index.html')
    context = {
        'movies': latest_movies,
    }
    return HttpResponse(template.render(context, req))


def detail(req, id):
    movie = Movie.objects.get(pk=id)
    cast = movie.cast.all()
    template = loader.get_template('detail.html')
    context = {
        'movie': movie,
        'cast': cast
    }
    return HttpResponse(template.render(context, req))
