from django.contrib import admin
from manager.models import Movie, DeliveryType, Director, Genre, Rating

admin.site.register(Movie)
admin.site.register(DeliveryType)
admin.site.register(Director)
admin.site.register(Genre)
admin.site.register(Rating)