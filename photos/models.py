from django.db import models
import datetime as dt

# Create your models here.
class Photographer(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()

    def __str__(self):
        return self.first_name
    
    def save_photographer(self):
        self.save()

class Location(models.Model):
    location = models.CharField(max_length = 40)

class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/')
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 150)
    image_location = models.ForeignKey(Location)





    
