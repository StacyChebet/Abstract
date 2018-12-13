from django.db import models
# import datetime as dt

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

    def __str__(self):
        return self.location

class Category(models.Model):
    category = models.CharField(max_length = 40)

    def __str__(self):
        return self.category


class Image(models.Model):
    image = models.ImageField(upload_to = 'pictures/')
    name = models.CharField(max_length = 30)
    description = models.CharField(max_length = 150)
    image_location = models.ForeignKey(Location, on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    @classmethod
    def search_by_title(cls,title):
        image = cls.objects.filter(name__icontains = title)
        return image



    
