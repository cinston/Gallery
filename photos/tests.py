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

    def test_instance(self):
        '''
        Test case to see if the object is an instance of the Location class.
        '''
        self.assertTrue(isinstance(self.location,Location))

    def test_save_method(self):
        '''
        Test case to see if the object is stored in the database.
        '''
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_update_method(self):
        '''
        Test case to see if the object can be retrieved from the database and updated.
        '''
        self.location.save_location()
        self.location = Location.objects.filter(name = 'Nairobi').update(name = 'Nakuru')
        self.updated_location = Location.objects.get(name = 'Nakuru')
        self.assertEqual(self.updated_location.name,"Nakuru")

    def test_delete_method(self):
        '''
        Test case to see if the object can be deleted from the database.
        '''
        self.location.save_location()
        self.location = Location.objects.get(id = 1)
        self.location.delete_location()
        self.assertTrue(len(Location.objects.all()) == 0)

class ImageTestClass(TestCase):
    '''
    Defines test cases for the Image class behaviours.
      
    Args:
        TestCase: A class that helps create the test cases.
    '''
    def setUp(self):
        '''
        Method that runs before the test cases.
        '''
        self.location = Location(name = "Nairobi")
        self.location.save_location()
        self.category = Category(name = "Test")
        self.category.save_category()
        self.image = Image(id = 1,name = "test", description = "test description", image_path = "path/to/image", category = self.category, location = self.location)

    def test_instance(self):
        '''
        Test case to see if the object is an instance of the Image class.
        '''
        self.assertTrue(isinstance(self.image,Image))

    def test_save_image(self):
        '''
        Test case to see if the object is stored in the database.
        '''
        self.image.save_image()
        self.images = Image.objects.all()
        self.assertTrue(len(self.images) > 0)

    def test_get_image_by_id(self):
        '''
        Test case to see if an specific image can be retrieved from the database.
        '''
        self.image.save_image()
        self.image = Image.get_image_by_id(1)
        self.assertTrue(isinstance(self.image,Image))

    def test_update_image(self):
        '''
        Test case to see if the object can be retrieved from the database and updated.
        '''
        self.image.save_image()
        self.image = Image.objects.filter(id = 1).update(image_path = "new/path/to/image")
        self.updated_image = Image.get_image_by_id(1)
        self.assertEqual(self.updated_image.image_path,"new/path/to/image")

    def test_search_by_category(self):
        '''
        Test case to see if images can be queried from the database based on the category.
        '''
        self.image.save_image()
        self.category = Category(name = "test")
        self.category.save_category()
        self.searched_images = Image.search_by_category('test')
        self.assertTrue(len(self.searched_images) > 0)

    def test_filter_by_location(self):
        '''
        Test case to see if images can be queried from the database based on the location.
        '''
        self.image.save_image()
        self.searched_images = Image.filter_by_location('Nairobi')
        self.assertTrue(len(self.searched_images) > 0)

    def test_delete_image(self):
        '''
        Test case to see if the object can be deleted from the database.
        '''
        self.image.save_image()
        self.searched_image = Image.get_image_by_id(1)
        self.searched_image.delete_image()
        self.assertTrue(len(Image.objects.all()) == 0)

class CategoryTestClass(TestCase):
    '''
    Defines test cases for the Category class behaviours.
      
    Args:
        TestCase: A class that helps create the test cases.
    '''
    def setUp(self):
        '''
        Method that runs before the test cases.
        '''
        self.category = Category(id = 1,name = 'test')

    def test_instance(self):
        '''
        Test case to see if the object is an instance of the Category class.
        '''
        self.assertTrue(isinstance(self.category,Category))

    def test_save_method(self):
        '''
        Test case to see if the object is stored in the database.
        '''
        self.category.save_category()
        self.Category = Category.objects.all()
        self.assertTrue(len(self.Category) > 0)

    def test_update_method(self):
        '''
        Test case to see if the object can be retrieved from the database and updated.
        '''
        self.category.save_category()
        self.category = Category.objects.filter(name = 'test').update(name = 'changed')
        self.updated_category = Category.objects.get(name = 'changed')
        self.assertEqual(self.updated_category.name,"changed")

    def test_delete_method(self):
        '''
        Test case to see if the object can be deleted from the database.
        '''
        self.category.save_category()
        self.category = Category.objects.get(id = 1)
        self.category.delete_category()
        self.assertTrue(len(Category.objects.all()) == 0)