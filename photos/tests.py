from django.test import TestCase
from .models import Photographer
import datetime as dt 

# Create your tests here.
class PhotographerTestClass(TestCase):
    #Set up method

    def setUp(self):
        self.stacy = Photographer(first_name = 'Stacy', last_name = 'Chebet', email = 'staceychebet23@gmail.com')

    #Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.stacy,Photographer))

    #Testing the save method
    def test_save_method(self):
        self.stacy.save_photographer()
        photographers = Photographer.objects.all()
        self.assertTrue(len(photographers)>0)


