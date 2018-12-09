from django.contrib import admin
from .models import Photographer,Image,Location

# Register your models here.
admin.site.register(Photographer)
admin.site.register(Image)
admin.site.register(Location)