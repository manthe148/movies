from django.db import models
from django.urls import reverse


class Genre(models.Model):
    """Genre of the movie """
    name = models.CharField(max_length=255, help_text='Enter movie genre here')
    def __str__(self):
        """ String shwoing the model object """
        return self.name


class DeliveryType(models.Model):
    """ DVD or VHS """
    delivered = models.CharField(max_length=3, help_text='Enter delivery type')
    def __str__(self):
        return self.delivered


class Rating(models.Model):
    """ Rating? """
    rated = models.CharField(max_length = 5)
    def __str__(self):
        return self.rated




class Movie(models.Model):
    title = models.CharField(max_length=200)

# ForeignKey used because a movie can only have one director, but directors can have multipule movies
    director = models.ForeignKey('Director', on_delete=models.SET_NULL, null = True)
    summery = models.TextField(max_length=1000, help_text='Enter a brief discription of the movie')

    genre = models.ManyToManyField(Genre, help_text='Select a genre for this movie')
    delivery = models.ManyToManyField(DeliveryType, help_text='Select delivery type for this movie')

    rating = models.ManyToManyField(Rating, help_text = 'What is the moved rated?')


    def __str__(self):
        """ String showing the model object """
        return self.title

    def get_absolute_url(self):
        """ Returns the url to access a detailed record for this movie """
        return reverse('movie-detail', args=[str(self.id)])



class Director(models.Model):
    """ Model showing the director """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    # class Meta:
        # ordering = ['first_name', ' last_name']
    
    def get_absolute_url(self):
        return reverse('director_detail', args=[str(self.first_name)])

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



