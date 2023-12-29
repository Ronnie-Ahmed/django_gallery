from django.test import TestCase
from app.models import PhotoCategory,PhotoGallery
from django.contrib.auth.models import User 

# Create your tests here.

class URLTest(TestCase):
    def test_checkurl(self):
        response=self.client.get('/Home')
        self.assertEqual(response.status_code,200)

class ModelTestCase(TestCase):
    
    
    def test_checkPhotoCategory(self):
        category=PhotoCategory.objects.create(category="Anime")
        self.assertEqual(str(category),"Anime")
        
    def test_checkPhotoGallery(self):
        category=PhotoCategory.objects.create(category="Anime")
        testinfo=PhotoGallery.objects.create(title="Anime",category=category)
        self.assertEqual(str(testinfo)," Title: Anime Category: Anime" )