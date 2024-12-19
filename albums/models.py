from django.db import models
from musicians.models import Musician

# Create your models here.


class Album(models.Model):
    album_name = models.CharField(max_length=50)
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE)
    album_release_date = models.DateTimeField(auto_now=True)
    class Rating(models.IntegerChoices):
        ONE = 1, 'Very Bad'
        TWO = 2, 'Bad'
        THREE = 3, 'Average'
        FOUR = 4, 'Good'
        FIVE = 5, 'Excellent'
    rating = models.IntegerField(choices=Rating.choices)

    def __str__(self):
        return self.album_name
