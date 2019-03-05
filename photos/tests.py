from django.test import TestCase
from .models import Image, Location, Category

# Create your tests here.
class LocationTestClass(TestCase):
    '''
    Defines test cases for the Location class behaviours.
      
    Args:
        TestCase: A class that helps create the test cases.
    '''
    def setUp(self):
        '''
        Method that runs before the test cases.
        '''
        self.location = Location(id = 1,name = 'Nairobi')