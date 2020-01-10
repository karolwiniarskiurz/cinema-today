from django.db import models

# Create your models here.
from people.models import Person

MOVIE_GENRES = [
    ('Comedy', 'Comedy'),
    ('Horror', 'Horror'),
    ('Drama', 'Drama'),
    ('Documentary', 'Documentary'),
    ('Action', 'Action'),
    ('Historic', 'Historic'),
    ('Thriller', 'Thriller')
]


class Movie(models.Model):
    title = models.CharField(max_length=512)
    description = models.CharField(max_length=2048)
    genre = models.CharField(choices=MOVIE_GENRES, max_length=32)
    release_year = models.IntegerField()
    country = models.CharField(max_length=512)
    duration = models.IntegerField(default=0)
    image = models.URLField()
    director = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name='director')
    writer = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True, related_name='scenarist')
    cast = models.ManyToManyField(Person)

    def __str__(self):
        return self.title
