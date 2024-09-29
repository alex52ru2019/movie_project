from django.db import models

# Create your models here.
class films_posts(models.Model):
    films_name = models.CharField(max_length=100) # название фильма
    films_text = models.TextField() # описание фильма
    films_review = models.TextField() # отзыв

    def __str__(self):
        return self.films_name

