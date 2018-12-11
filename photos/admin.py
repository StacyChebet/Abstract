from django.contrib import admin
from .models import Photographer,Image,Location,Category


# Register your models here.
admin.site.register(Photographer)
admin.site.register(Image)
admin.site.register(Location)
admin.site.register(Category)