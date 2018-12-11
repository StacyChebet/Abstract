from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image,Category,Location


# Create your views here.
def all_photos(request):
    images = Image.objects.all()

    return render(request, 'index.html', {"images":images} )

