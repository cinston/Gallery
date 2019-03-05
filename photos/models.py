from django.db import models

# Create your models here.
class Category(models.Model):
    '''
    Category class that creates category objects.
    '''
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_category(self):
        '''
          Method that saves the categories in the database.
        '''
        self.save()

    def update_category(self, cate):
        '''
          Method that updates the categories in the database.
        '''
        self.update(name = cate)

    def delete_category(self):
        '''
          Method that deletes the categories in the database.
        '''
        self.delete()

class Location(models.Model):
    '''
    Location class that creates location objects.
    '''
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name

    def save_location(self):
        '''
          Method that saves the locations in the database.
        '''
        self.save()

    def update_location(self, loc):
        '''
          Method that updates the locations in the database.
        '''
        self.update(name = loc)

    def delete_location(self):
        '''
          Method that deletes the locations in the database.
        '''
        self.delete()
    
class Image(models.Model):
    '''
    Image class that creates image objects.
    '''
    name = models.CharField(max_length = 30)
    description = models.TextField()
    image_path = models.ImageField(upload_to = 'images/')
    category = models.ForeignKey(Category)
    location = models.ForeignKey(Location)

    def __str__(self):
        return self.name

    def save_image(self):
        '''
          Method that saves the images in the database.
        '''
        self.save()

    def update_image(self, img):
        '''
          Method that updates the images in the database.
        '''
        self.update(name = img)

    def delete_image(self):
        '''
          Method that deletes the images in the database.
        '''
        self.delete()

    @classmethod
    def all_images(cls):
        '''
          Method that returns all the images in the database.
        '''
        images = cls.objects.all()
        return images

    @classmethod
    def search_by_category(cls,search_term):
        '''
          Method that retrieves an image in the database based on the category.
        '''
        images = cls.objects.filter(category__name__contains = search_term)
        if len(images) < 1:
            case_images = cls.objects.filter(category__name__contains = search_term.capitalize())
            return case_images
        else:
            return images

    @classmethod
    def get_image_by_id(cls,id):
        '''
          Method that retrieves an image in the database based on its id.
        '''
        image = cls.objects.get(id = id)
        return image

    @classmethod
    def filter_by_location(cls,search_term):
        '''
          Method that filters images in the database based on the location.
        '''
        location = Location.objects.get(name = search_term)
        images = cls.objects.filter(location = location)
        return images