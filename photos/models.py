from django.db import models
import datetime as dt

# Create your models here.

class Photographer(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phone_number = models.CharField(max_length = 10, blank = True)

    def __str__(self):
        return self.first_name
    
    def save_photographer(self):
        self.save()

class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/')
    title = models.CharField(max_length = 60)
    description = models.CharField()
    image_location = models.ForeignKey(Location)
    image_category = models.ForeignKey(Category)

    
